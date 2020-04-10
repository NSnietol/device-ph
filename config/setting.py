
from pathlib import Path 

from dotenv import load_dotenv

import config.logsmanager as log

load_dotenv()

env_path = Path('.') / '.env'
log.logger.info(' Device ON ')
load_dotenv(dotenv_path=env_path)
log.logger.info('.env loaded :) ')
