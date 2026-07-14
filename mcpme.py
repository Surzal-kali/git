from mcp.server import Server
from mcp.types import Tool, TextContent
from fastapi import FastAPI, Request, HTTPException
import subprocess
import logging
import re
import uuid
import asyncio
from datetime import datetime
from enum import Enum
import uvicorn 

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI(title="Kali Terminal MCP Server")

# Job state enum
class JobState(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

# In-memory job store
jobs_store = {} 

# Tool definitions
KALI_COMMAND_TOOL = {
    "name": "kali_command",
    "description": "Execute commands on Kali terminal asynchronously",
    "inputSchema": {
        "type": "object",
        "properties": {"command": {"type": "string"}},
        "required": ["command"]
    }
}

JOB_STATUS_TOOL = {
    "name": "job_status",
    "description": "Check the status and results of a command job",
    "inputSchema": {
        "type": "object",
        "properties": {"job_id": {"type": "string"}},
        "required": ["job_id"]
    }
}

def validate_command(command: str) -> tuple[bool, str]:
    """Validate command for security issues. Returns (is_valid, error_message)"""
    if not command:
        return False, "Command cannot be empty"
    
    # Block obvious shell injection patterns
    dangerous_patterns = [r'\|\|', r'\$\(', r'`', r';']
    for pattern in dangerous_patterns:
        if re.search(pattern, command):
            logger.warning(f"Blocked command with dangerous pattern: {command}")
            return False, f"Command contains forbidden pattern. Avoid: &&, ||, $(, backticks, ;, |"
    
    return True, ""


async def execute_command_background(job_id: str, command: str):
    """Execute a command in the background and store results"""
    try:
        jobs_store[job_id]["status"] = JobState.RUNNING
        jobs_store[job_id]["started_at"] = datetime.now().isoformat()
        
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        
        jobs_store[job_id]["status"] = JobState.COMPLETED
        jobs_store[job_id]["output"] = result.stdout
        jobs_store[job_id]["completed_at"] = datetime.now().isoformat()
        logger.info(f"Job {job_id} completed successfully: {command}")
        
    except subprocess.CalledProcessError as e:
        jobs_store[job_id]["status"] = JobState.FAILED
        jobs_store[job_id]["output"] = e.stderr
        jobs_store[job_id]["error"] = str(e)
        jobs_store[job_id]["completed_at"] = datetime.now().isoformat()
        logger.error(f"Job {job_id} failed with error: {e}")
        
    except Exception as e:
        jobs_store[job_id]["status"] = JobState.FAILED
        jobs_store[job_id]["error"] = str(e)
        jobs_store[job_id]["completed_at"] = datetime.now().isoformat()
        logger.exception(f"Job {job_id} unexpected error: {command}")


def submit_command_job(command: str) -> dict:
    """Submit a command to run asynchronously. Returns job_id."""
    job_id = str(uuid.uuid4())
    
    jobs_store[job_id] = {
        "job_id": job_id,
        "command": command,
        "status": JobState.PENDING,
        "created_at": datetime.now().isoformat(),
        "output": None,
        "error": None
    }
    
    # Create background task to execute command
    asyncio.create_task(execute_command_background(job_id, command))
    
    logger.info(f"Job {job_id} submitted for command: {command}")
    return {"type": "text", "text": f"Job submitted with ID: {job_id}"}


def get_job_status(job_id: str) -> dict:
    """Get the status of a job"""
    if job_id not in jobs_store:
        return {"type": "error", "text": f"Job {job_id} not found"}
    
    job = jobs_store[job_id]
    return {
        "type": "text",
        "text": f"""Job Status Report:
ID: {job['job_id']}
Command: {job['command']}
Status: {job['status']}
Created: {job['created_at']}
Started: {job.get('started_at', 'N/A')}
Completed: {job.get('completed_at', 'N/A')}

Output:
{job.get('output', 'No output yet')}

Error:
{job.get('error', 'No errors')}"""
    }


# JSON-RPC 2.0 MCP Protocol Implementation

@app.get("/")
async def mcp_get():
    """GET endpoint for discovery/info"""
    return {
        "name": "kali-terminal",
        "version": "1.0.0",
        "protocolVersion": "2024-11-05"
    }


@app.post("/")
async def mcp_endpoint(request: Request):
    """Main MCP JSON-RPC 2.0 endpoint"""
    try:
        body = await request.json()
    except Exception as e:
        logger.error(f"Failed to parse JSON: {e}")
        return {
            "jsonrpc": "2.0",
            "error": {"code": -32700, "message": "Parse error"},
            "id": None
        }
    
    jsonrpc = body.get("jsonrpc", "2.0")
    method = body.get("method")
    params = body.get("params", {})
    request_id = body.get("id")
    
    logger.info(f"MCP Request - Method: {method}, ID: {request_id}")
    
    # Handle initialize
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "serverInfo": {
                    "name": "kali-terminal",
                    "version": "1.0.0"
                }
            },
            "id": request_id
        }
    
    # Handle tools/list
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "result": {"tools": [KALI_COMMAND_TOOL, JOB_STATUS_TOOL]},
            "id": request_id
        }
    
    # Handle tools/call
    elif method == "tools/call":
        tool_name = params.get("name")
        arguments = params.get("arguments", {})
        
        if tool_name == "kali_command":
            command = arguments.get("command", "")
            
            # Validate command
            is_valid, error_msg = validate_command(command)
            if not is_valid:
                return {
                    "jsonrpc": "2.0",
                    "result": {
                        "content": [{"type": "error", "text": error_msg}],
                        "isError": True
                    },
                    "id": request_id
                }
            
            result = submit_command_job(command)
            return {
                "jsonrpc": "2.0",
                "result": {
                    "content": [result],
                    "isError": False
                },
                "id": request_id
            }
        
        elif tool_name == "job_status":
            job_id = arguments.get("job_id", "")
            result = get_job_status(job_id)
            return {
                "jsonrpc": "2.0",
                "result": {
                    "content": [result],
                    "isError": result.get("type") == "error"
                },
                "id": request_id
            }
        
        else:
            return {
                "jsonrpc": "2.0",
                "error": {"code": -32602, "message": f"Unknown tool: {tool_name}"},
                "id": request_id
            } 
    
    # Unknown method (just in case)
    else:
        return {
            "jsonrpc": "2.0",
            "error": {"code": -32601, "message": f"Method not found: {method}"},
            "id": request_id
        }


@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy", "service": "kali-terminal-mcp"}


# Run via HTTP
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)

