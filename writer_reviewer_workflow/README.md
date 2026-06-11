# Writer Reviewer Workflow

This app uses Microsoft Agent Framework to run a writer-reviewer collaboration against a local OpenAI-compatible model endpoint.

Flow:

1. The writer agent drafts content from the user request.
2. The reviewer agent returns concise, actionable feedback.
3. The writer refines the draft using that feedback.
4. The final output is plain text containing the refined content.

The workflow module also exposes synchronous and asynchronous helpers so it can be called from a REPL.

## Local setup

```bash
cd writer_reviewer_workflow
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
python -m writer_reviewer_workflow.app "Write a launch announcement for a local AI meetup"
```

To inspect the intermediate stages:

```bash
python -m writer_reviewer_workflow.app --show-stages "Draft a short blog intro about secure coding"
```
