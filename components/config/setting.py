
from pathlib import Path

from dotenv import load_dotenv
from loguru import logger
from components.property_manager import get_property_value
from components.utils.thread_util import execute_background
import requests

load_dotenv()

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
logger.info(' .env done :)')

""" Heroku server sleeps each seven hours every day. so I active the server before requests """
def asyn_activation_heroku():

    try:

        requests.get(get_property_value('url.phman'), None, verify=False, timeout=2)
        requests.get(get_property_value('url.sgph'), None, verify=False, timeout=2)
        logger.info('Activing heroku servers')
    except Exception:
        pass


execute_background(asyn_activation_heroku)
