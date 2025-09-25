# ai-agent

> Thanks to [`boot.dev`](https://www.boot.dev) for this guided project

## Requirements

- Python >= 3.13
- `google-genai`
- `python-dotenv`
- `GEMINI_API_KEY` (see [here](https://ai.google.dev/gemini-api/docs/api-key)

## Quick Start

> Inside a `.env` file (or whatever tools you use to manage env vars) define `GEMINI_API_KEY`

```sh
git clone https://github.com/moxcz/ai-agent
cd ai-agent
python3 -m venv .venv
. ./.venv/bin/activate
pip install -r requirements.txt
export GEMINI_API_KEY=<your-key-goes-here>
python3 main.py
```

Or, if you have `uv` installed (you should, see [here](https://docs.astral.sh/uv/getting-started/installation/):

```sh
uv venv
. ./.venv/bin/activate
uv sync
uv run main.py
```

You can also just use my `Makefile`:

```sh
make install
python3 main.py
```

