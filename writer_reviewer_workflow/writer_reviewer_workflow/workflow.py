from __future__ import annotations

import asyncio
import os
from dataclasses import dataclass

from agent_framework import Agent, Executor, WorkflowBuilder, WorkflowContext, executor, handler
from agent_framework.openai import OpenAIChatClient
from dotenv import load_dotenv
from typing_extensions import Never


WRITER_INSTRUCTIONS = """You are a precise content writer.
Draft clear, well-structured plain text that directly answers the user's request.
Do not mention internal workflow steps.
"""

REVIEWER_INSTRUCTIONS = """You are a concise reviewer.
Provide short, actionable feedback that improves clarity, correctness, structure, and tone.
Keep feedback compact and plain text.
"""


@dataclass(slots=True)
class DraftPayload:
    request: str
    draft: str


@dataclass(slots=True)
class ReviewPayload:
    request: str
    draft: str
    feedback: str


def _load_local_model_env() -> None:
    load_dotenv(override=False)
    os.environ.setdefault("OPENAI_BASE_URL", "http://localhost:11434/v1")
    os.environ.setdefault("OPENAI_MODEL", "local-model")
    os.environ.setdefault("OPENAI_API_KEY", "local-model")


def _create_agents() -> tuple[Agent, Agent]:
    _load_local_model_env()
    client = OpenAIChatClient()

    writer = Agent(
        name="WriterAgent",
        instructions=WRITER_INSTRUCTIONS,
        client=client,
    )
    reviewer = Agent(
        name="ReviewerAgent",
        instructions=REVIEWER_INSTRUCTIONS,
        client=client,
    )
    return writer, reviewer


class WriterDraftExecutor(Executor):
    def __init__(self, writer: Agent) -> None:
        super().__init__(id="writer_draft")
        self._writer = writer

    @handler
    async def write(self, request: str, ctx: WorkflowContext[DraftPayload, str]) -> None:
        response = await self._writer.run(
            "Write an initial draft for the following request. Return plain text only.\n\n"
            f"Request:\n{request}"
        )
        draft = response.text.strip()
        await ctx.yield_output(draft)
        await ctx.send_message(DraftPayload(request=request, draft=draft))


def create_workflow():
    writer, reviewer = _create_agents()

    @executor(id="reviewer_feedback")
    async def reviewer_feedback(payload: DraftPayload, ctx: WorkflowContext[ReviewPayload, str]) -> None:
        response = await reviewer.run(
            "Review the following draft and provide concise, actionable feedback in plain text.\n\n"
            f"Original request:\n{payload.request}\n\n"
            f"Draft:\n{payload.draft}"
        )
        feedback = response.text.strip()
        await ctx.yield_output(feedback)
        await ctx.send_message(
            ReviewPayload(
                request=payload.request,
                draft=payload.draft,
                feedback=feedback,
            )
        )

    @executor(id="writer_refine")
    async def writer_refine(payload: ReviewPayload, ctx: WorkflowContext[Never, str]) -> None:
        response = await writer.run(
            "Revise the draft using the review feedback. Return only the refined content in plain text.\n\n"
            f"Original request:\n{payload.request}\n\n"
            f"Draft:\n{payload.draft}\n\n"
            f"Reviewer feedback:\n{payload.feedback}"
        )
        refined = response.text.strip()
        await ctx.yield_output(refined)

    draft_executor = WriterDraftExecutor(writer)
    return (
        WorkflowBuilder(start_executor=draft_executor)
        .add_edge(draft_executor, reviewer_feedback)
        .add_edge(reviewer_feedback, writer_refine)
        .build()
    )


async def run_writer_reviewer(request: str) -> str:
    events = await create_workflow().run(request)
    outputs = [str(output).strip() for output in events.get_outputs() if str(output).strip()]
    if not outputs:
        raise RuntimeError("The workflow completed without producing any output.")
    return outputs[-1]


async def run_writer_reviewer_trace(request: str) -> dict[str, str]:
    events = await create_workflow().run(request)
    outputs = [str(output).strip() for output in events.get_outputs() if str(output).strip()]
    result = {
        "draft": outputs[0] if len(outputs) > 0 else "",
        "feedback": outputs[1] if len(outputs) > 1 else "",
        "refined": outputs[-1] if outputs else "",
    }
    return result


def run_writer_reviewer_sync(request: str) -> str:
    return asyncio.run(run_writer_reviewer(request))
