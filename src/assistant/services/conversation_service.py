from assistant.models.conversation import Conversation
from assistant.providers.llm_provider import llm_provider
from assistant.models.conversation import Conversation
from assistant.models.message import MessageRole
import logging

logger = logging.getLogger(__name__)

class ConversationService:
    def __init__(self, system_prompt: str):
        logger.info("Initializing ConversationService")
        self.conversations: Conversation = Conversation()  
        self.conversations.add_message(MessageRole.SYSTEM, system_prompt)

    def add_conversation(self, user_prompt: str):
        self.conversations.add_message(MessageRole.USER, user_prompt)

    def add_assistant_converstaion(self, assistant_prompt: str):
        self.conversations.add_message(MessageRole.ASSISTANT, assistant_prompt)

    def get_conversation(self) -> Conversation:
        return self.conversations
