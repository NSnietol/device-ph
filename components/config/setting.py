
from pathlib import Path 

from dotenv import load_dotenv
from loguru import logger


load_dotenv()

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
logger.info(' .env done :)')
