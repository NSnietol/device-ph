
if __name__ == '__main__':
    from config.setting import *
    from config.logsmanager import logger;
    from components.property_manager import getPropertyValue

    logger.info("current env "+ str(getPropertyValue("url.phman")))

