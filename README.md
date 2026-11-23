# anvil-llm-lab

Course notebooks from [Alexey Grigorev's AI Engineering Bootcamp](https://maven.com/) (Maven). Hands-on work through LLM APIs, RAG, tool calling, and agent frameworks — kept flat at the repo root so you can open any notebook immediately.

## Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)
- An OpenAI API key

## Setup

```bash
git clone https://github.com/26th247/anvil-llm-lab.git
cd anvil-llm-lab
uv sync
```

Create a `.env` in the repo root (gitignored):

```env
OPENAI_API_KEY=sk-...
```

Start Jupyter from the project env:

```bash
uv run jupyter notebook
```

Or open notebooks in Cursor/VS Code and pick the `.venv` kernel (`anvil-llm-lab`).

## Layout

```text
foundations-llm-rag-search/   # week 1 — OpenAI API, RAG, structured output
agents/
  agentic_rag/                # week 2 — tool calling + agentic loops
  agentic_frameworks/         # week 3 — ToyAIKit, PydanticAI, homework
```

### Foundations (LLM + RAG + search)

| Notebook | Focus |
| --- | --- |
| `01-openai_api.ipynb` | Chat Completions basics |
| `02-retrieval_augmented_generation.ipynb` | Chunking, indexing with minsearch, RAG Q&A |
| `03-structured_output.ipynb` | Structured / typed model outputs |
| `03.1-streaming_structured_output.ipynb` | Streaming structured responses |
| `04-homework.ipynb` | Week 1 homework (PDF → markdown → RAG) |

### Agentic RAG

| Notebook | Focus |
| --- | --- |
| `01-agentic_rag_and_tool_calling.ipynb` | Tools + function calling beyond plain RAG |
| `02-agentic_loop.ipynb` | Manual agent loop (model ↔ tools) |
| `03-q&a_loop_with_agent_library.ipynb` | Same loop with a small agent library |

### Agent frameworks

| Notebook | Focus |
| --- | --- |
| `01-agent_frameworks_and_implementation.ipynb` | ToyAIKit intro |
| `02-organising_tools_in_a_class.ipynb` | Tool classes + auto-registration |
| `03-going-beyond-rag.ipynb` | Search + fetch tools (snippet vs full doc) |
| `04-pydanticai-prod-ready-agents.ipynb` | PydanticAI agents |
| `05-homework.ipynb` | Wikipedia agent homework (search/fetch, Q1–Q6) |
| `search_tools.py` | Shared search helpers used by the frameworks notebooks |

## Stack

Managed in `pyproject.toml` via uv (lockfile committed):

- **LLM / agents:** `openai`, `pydantic-ai`, `toyaikit`
- **RAG / docs:** `minsearch`, `markitdown`, `gitsource`, `python-frontmatter`
- **Notebooks:** `jupyter`, `nest-asyncio`, `python-dotenv`, `requests`

## Notes

- This repo is notebooks-only (`package = false`). There is no installable Python package.
- On Windows, top-level `await` with PydanticAI can kill the Jupyter kernel. Prefer `nest_asyncio` + `run_sync` (see `04-pydanticai-prod-ready-agents.ipynb`).
- Large homework data dirs like `books/` are gitignored; regenerate them from the notebooks when needed.
