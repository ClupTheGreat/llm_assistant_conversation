import ollama
import logging
from assistant.providers.llm_provider import llm_provider
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

    def chat_stream(self, user_prompt: str):
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
