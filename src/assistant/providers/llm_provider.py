from assistant.models.conversation import Conversation

class llm_provider():
    def __init__(self, model_arg:str):
        self.model_provided: str = model_arg

#    def chat_stream(self, user_prompt: str):
#         yield from ()
    def chat_stream(self, user_prompt: Conversation):
        yield from()
