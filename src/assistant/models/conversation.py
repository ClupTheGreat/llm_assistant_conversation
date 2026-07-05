from dataclasses import dataclass, field
from assistant.models.message import Message, MessageRole

@dataclass
class Conversation:
    messages: list[Message] = field(default_factory=list)

    def add_message(self, role: MessageRole, content: str):
        self.messages.append(Message(role=role, content=content))
