from assistant.cli.commands import run
from pathlib import Path
import logging

log_dir = Path(__file__).parent / "logs"
log_dir.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s %(name)s: %(message)s]',
    handlers=[
        logging.FileHandler(log_dir / 'application.log')
    ]
)

def main():
    run()


if __name__ == "__main__":
    main()
