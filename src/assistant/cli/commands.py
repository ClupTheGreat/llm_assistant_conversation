# imports for application
from assistant.cli.parser import cli_parser
from assistant.services.chat import ChatService
from assistant.services.conversation_service import ConversationService
from assistant.providers.ollama_provider import OllamaProvider

# general imports
import itertools
import threading
import sys
import time
import logging
from random import randint
logger = logging.getLogger(__name__)


# Helper stuff

# Temporary name
username = "Clup"
assistant_name = "Agent M"
# Stolen from Gippity
list_of_greet_messages = ["Ready when you are.", "What's on the agenda today?", f"How can I help, {username}" ]

# Animation

def animate(loading: threading.Event):
    # Simple CLI animation, loading spinner
    for c in itertools.cycle(['|','/','-','\\']):
        if loading.is_set():
            break
        sys.stdout.write('\rthinking ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')

# Greet Randomizer

def greet_randomizer() -> str:
    random_int = randint(0, len(list_of_greet_messages) - 1)
    greet = list_of_greet_messages[random_int]
    return greet


#  ----------------------------------------------------------------------------

# Flag for thinking animation thread
loading = threading.Event() 
# Starting another thread for thinking animation to not block the
# main thread.
thinking_thread = threading.Thread(target=animate, args=(loading,))

# Handling different flags from the user

def handle_ask(args, chat_service: ChatService):
    logger.info("Handling ask")

    # Creating conversation
    system_prompt = "You are a helpful CLI assistant"
    conversation_single = ConversationService(system_prompt=system_prompt)
    conversation_single.add_conversation(args)
    
    #for piece in chat_service.ask_streaming(args):
    for piece in chat_service.ask_streaming(conversation_single.get_conversation()):
        # Handles the empty spaces in the cli with thinking animation
        if piece != '':
            logger.debug("First token detected for stream, stopping spinner animation")
            loading.set() 
            thinking_thread.join()
        # Printing as a stream from LLM
        print(piece, end='', flush=True)

def handle_chat(args, chat_service: ChatService):
    logger.info("Handling Chat")
    loading.set()
    thinking_thread.join()
    
    # Creating a long conversation
    system_prompt = "You are a helpful CLI assistant"
    conversation_long = ConversationService(system_prompt=system_prompt)

    greet = greet_randomizer()
    print(greet)
    while True:
        user_input: str = input(" You > ")
        conversation_long.add_conversation(user_input)
#        loading.clear()
#        thinking_thread.start()
        assistant_convo: str = ""
#        print(assistant_name + " > ")
        for piece in chat_service.ask_streaming(conversation_long.get_conversation()):
            if piece != '':
                logger.debug("First token detected for stream, stopping spinner animation")
#                loading.set() 
#                thinking_thread.join()
                assistant_convo = assistant_convo + piece
            # Printing as a stream from LLM
            print(piece, end='', flush=True)
        print("\n")
        conversation_long.add_assistant_conversation(assistant_convo)
    pass


# run() will be called by the main function, this acts as the entry point to the software
def run():
    # We will eventually accept a model from the user if provided, but we will use a placeholder model
    # for now.
    
    # Initialize chat model
    use_model = "qwen3.5:9b"
    logger.info("Initializing chat service with model =%s", use_model)
    # Initializing an llm provider
    llmProvider = OllamaProvider(model_arg=use_model)
    chat_service = ChatService(model=use_model, provider=llmProvider)
    
    # Accept arguments from the user
    args = cli_parser()


    if args is None:
        logger.warning("No args provided by the user")
        print("Please provide some input")
    else:
        logger.debug("Starting spinner thread")
        thinking_thread.start()
        
        try:
            if args.ask:
                handle_ask(args.ask, chat_service=chat_service)
            if args.chat:
                handle_chat(args.chat, chat_service=chat_service)
        except Exception:
            logger.exception("Error while streaming response from chat_service")
            loading.set()
            thinking_thread.join()
            raise
        print("\n")
        logger.info("Prompt responded to by chat_service")
        if thinking_thread.is_alive():
            logger.error("Thinking thread never ended, which means the try and except both failed, probably an error")
            loading.set()
            thinking_thread.join()
