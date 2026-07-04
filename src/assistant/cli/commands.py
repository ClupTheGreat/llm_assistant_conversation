# imports for application
from assistant.cli.parser import cli_parser
from assistant.services.chat import ChatService

# general imports
import itertools
import threading
import sys
import time
import logging
logger = logging.getLogger(__name__)

def animate(loading: threading.Event):
    # Simple CLI animation, loading spinner
    for c in itertools.cycle(['|','/','-','\\']):
        if loading.is_set():
            break
        sys.stdout.write('\rthinking ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')

def run():
    # We will eventually accept a model from the user if provided, but we will use a placeholder model
    # for now.
    
    # Initialize chat model
    use_model = "qwen3.5:9b"
    logger.info("Initializing chat service with model =%s", use_model)
    chat_service = ChatService(model=use_model)
    
    # Accept arguments from the user
    args = cli_parser()

    # Flag for thinking animation thread
    loading = threading.Event() 

    if args is None:
        logger.warning("No args provided by the user")
        print("Please provide some input")
    else:
        # Starting another thread for thinking animation to not block the
        # main thread.
        thinking_thread = threading.Thread(target=animate, args=(loading,))
        logger.debug("Starting spinner thread")
        thinking_thread.start()
        
        try:
            for piece in chat_service.ask_streaming(args):

                # Handles the empty spaces in the cli with thinking animation
                if piece != '':
                    logger.debug("First token detected for stream, stopping spinner animation")
                    loading.set() 
                    thinking_thread.join()

                # Printing as a stream from LLM
                print(piece, end='', flush=True)
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
