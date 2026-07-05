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

### Handling Messages

Messages will be handled through Conversation and Conversation service.

1. Message models will have the three roles, "system", "user" and "assistant" role where they contain the inital prompt we pass in and in future the RAG content, tools etc, the prompt which the user sends, the prompt llm replied with respectively.

We also will happen to add on any extra context we retrieve from later on in the user prompts since we dont want to add more system prompts to avoid bugs. 

We will have timestamps which define at what time the messages were sent, possibly for arraging data around for saving messages later on.

One unique ID for identifying conversations so the user can get back to any of the conversations they were at.

Obviously a title for the previous unique ID, human readable.

This should be included in the meta-data.

2. The Conversation object should support: Adding a system message, this might or might not contain additional context. We can either add more functions, or add a flag which adds context of RAG etc to it. Adding a user message. Adding an assistant message. Get all messages which combines the 3, and returns the message's dictionary.

3. These classes live inside /conversation, the chat.py calls em and gets combined there, correct me if better exists.

4. Can't think of tradeoffs yet.

Introducting a new input, "--chat" or "-c", this will be interactive and this would also contain conversation history. Ask is for one off questions, chat would contain history and this.

exit would be with /exit command



