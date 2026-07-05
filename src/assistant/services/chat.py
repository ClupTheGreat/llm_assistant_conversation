from assistant.providers.ollama_provider import OllamaProvider
from assistant.providers.llm_provider import llm_provider 
import logging
from assistant.models.conversation import Conversation

# Creating log object
logger = logging.getLogger(__name__)

class ChatService:
    def __init__(self, model: str, provider: llm_provider):
        logger.info("Initializing ChatService")
        # Have this be moved to the main lunch sequence, so chatservice doesn't have to deal with having a provider, rather we would pass on this provider to this service.
        # self.provider: ollama_provider = OllamaProvider(model)

        # we will now provide an llm provider through arguments
        self.provider: llm_provider = provider

    def ask_streaming(self, prompt: Conversation):
        try:
            for streaming_chat in self.provider.chat_stream(prompt):
                yield streaming_chat
            logger.info("Streaming response recieved from Ollama")
        except Exception:
            logger.error("Error while streaming output from OllamaProvider")
            raise

#    def ask_streaming_old(self, prompt: str):
#        try:
#            for streaming_chat in self.provider.chat_stream_old(prompt):
#                yield streaming_chat
#            logger.info("Streaming response recieved from Ollama")
#        except Exception:
#            logger.error("Error while streaming output from OllamaProvider")
#            raise

    # Probably wont be using
#    def ask(self, prompt: str):
#        response = self.provider.chat(prompt)
#        return response
