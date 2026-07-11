from mcp.server import Server
from mcp.types import Tool, TextContent
from fastapi import FastAPI, Request, HTTPException
import subprocess
import logging
import re
import uvicorn

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI(title="Kali Terminal MCP Server")

# Tool definition
KALI_COMMAND_TOOL = {
    "name": "kali_command",
    "description": "Execute commands on Kali terminal",
    "inputSchema": {
        "type": "object",
        "properties": {"command": {"type": "string"}},
        "required": ["command"]
    }
}


async def execute_kali_command(command: str) -> dict:
    """Execute a command with security checks"""
    if not command:
        return {"type": "error", "text": "Command cannot be empty"}
    
    # Block obvious shell injection patterns
    dangerous_patterns = [r'&&', r'\|\|', r'\$\(', r'`', r';', r'\|']
    for pattern in dangerous_patterns:
        if re.search(pattern, command):
            logger.warning(f"Blocked command with dangerous pattern: {command}")
            return {"type": "error", "text": f"Command contains forbidden pattern. Avoid: &&, ||, $(, backticks, ;, |"}
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        logger.info(f"Command executed successfully: {command}")
        return {"type": "text", "text": result.stdout}
    except subprocess.CalledProcessError as e:
        logger.error(f"Command failed with error: {e}")
        return {"type": "error", "text": f"Error executing command: {e.stderr}"}
    except Exception as e:
        logger.exception(f"Unexpected error occurred while executing command: {command}")
        return {"type": "error", "text": f"An unexpected error occurred: {str(e)}"}


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
            "result": {"tools": [KALI_COMMAND_TOOL]},
            "id": request_id
        }
    
    # Handle tools/call
    elif method == "tools/call":
        tool_name = params.get("name")
        arguments = params.get("arguments", {})
        
        if tool_name != "kali_command":
            return {
                "jsonrpc": "2.0",
                "error": {"code": -32602, "message": f"Unknown tool: {tool_name}"},
                "id": request_id
            }
        
        command = arguments.get("command", "")
        result = await execute_kali_command(command)
        
        return {
            "jsonrpc": "2.0",
            "result": {
                "content": [result],
                "isError": result.get("type") == "error"
            },
            "id": request_id
        }
    
    # Unknown method
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
