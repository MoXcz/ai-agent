# ai-agent

> Thanks to [`boot.dev`](https://www.boot.dev) for this guided project

## Requirements

- Python >= 3.13
- `google-genai`
- `python-dotenv`

## Quick Start

```sh
git clone https://github.com/moxcz/ai-agent
cd ai-agent
python3 -m venv .venv
. ./.venv/bin/activate
pip install -r requirements.txt
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

