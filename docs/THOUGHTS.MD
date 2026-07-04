We will use uv project manager, which probably isn't required at this point.

Currently I will use argparse standard python library to parse command line arguments.

I will try to write tests on my own using pytest and make full use of logging library from python.

On this project, I will use Qwen3:8b model running locally using ollama.

assistant/

├── pyproject.toml
├── uv.lock
├── README.md
├── main.py
│
├── assistant/
│   ├── __init__.py
│   │
│   ├── cli/
│   │   ├── parser.py
│   │   └── commands.py
│   │
│   ├── providers/
│   │   ├── base.py
│   │   └── ollama_provider.py
│   │
│   ├── services/
│   │   └── chat.py
│   │
│   ├── config.py
│   └── exceptions.py
│
├── tests/
│
└── docs/
