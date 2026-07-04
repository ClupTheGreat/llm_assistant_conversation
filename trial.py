import os
import ollama

print({os.environ.get('OLLAMA_HOST')})

messages = [
    {"role": "user", "content" : "Hello World"}
]

response = ollama.chat(
    model = "qwen3.5:9b",
    messages=messages
)

print(response.message.content)
