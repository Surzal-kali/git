from __future__ import annotations

import argparse
import asyncio

from .workflow import run_writer_reviewer, run_writer_reviewer_trace


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the writer-reviewer Agent Framework workflow against a local model endpoint."
    )
    parser.add_argument("request", help="The user request for the writer-reviewer collaboration.")
    parser.add_argument(
        "--show-stages",
        action="store_true",
        help="Print the draft, review feedback, and refined result.",
    )
    return parser.parse_args()


async def _main() -> None:
    args = _parse_args()
    if args.show_stages:
        result = await run_writer_reviewer_trace(args.request)
        print("Draft:\n")
        print(result["draft"])
        print("\nReview Feedback:\n")
        print(result["feedback"])
        print("\nRefined Content:\n")
        print(result["refined"])
        return

    print(await run_writer_reviewer(args.request))


if __name__ == "__main__":
    asyncio.run(_main())