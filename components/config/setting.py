
from pathlib import Path 

from dotenv import load_dotenv
from loguru import logger
from components.property_manager import get_property_value
from components.utils.thread_util import execute_background
from requests import Session

load_dotenv()

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
logger.info(' .env done :)')

""" Heroku sleep a minimum of seven hours every day. so I active the server """
def asyn_activation_heroku():

    try:
        session = Session()
        session.get(get_property_value('url.phman'))
        session.get(get_property_value('url.sgph'))
        logger.info('Activing heroku servers')
    except Exception:
        pass
    
execute_background(asyn_activation_heroku)