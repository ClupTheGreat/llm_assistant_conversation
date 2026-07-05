import ollama
import logging
from assistant.providers.llm_provider import llm_provider
from assistant.models.conversation import Conversation
# Provides a class to connect to ollama chat


# Messages can have the role of system, user, assistant or tool
# Lookup usage for each

# Logging
logger = logging.getLogger(__name__)

class OllamaProvider(llm_provider):
    def __init__(self, model_arg: str):
        super().__init__(model_arg)
        logger.info("OllamaProvider initialized")
#        self.model_provided:str = model_arg

    def chat_stream(self, user_prompt: Conversation):
        # Connect to the model, send a message and get a respons
        # It can either be streaming or normal
        try:
            ollama_message = [{"role":msg.role, "content": msg.content} for msg in user_prompt.messages]

            stream = ollama.chat(
                model = self.model_provided,
                messages=ollama_message,
                stream = True,
            )

            for chunk in stream:
                yield chunk['message']['content']

        except Exception:
            logger.error("Couldn't connect to ollama")
            yield "Couldn't connect to ollama"
            raise

    def chat_stream_old(self, user_prompt: str):
        # Connect to the model, send a message and get a respons
        # It can either be streaming or normal
        try:
            stream = ollama.chat(
                model = self.model_provided,
                messages=[{'role':'user', 'content':f'{user_prompt}'}],
                stream = True,
            )

            for chunk in stream:
                yield chunk['message']['content']

        except Exception:
            logger.error("Couldn't connect to ollama")
            yield "Couldn't connect to ollama"
            raise


    # Probably wont be used, possibly depricate later
    def chat(self, user_prompt: str) -> str:
        response: ollama.ChatResponse = ollama.chat(
            model = self.model_provided,
            messages=[{'role':'user', 'content':f'{user_prompt}'}],
        )
        return response['message']['content']
