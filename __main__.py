
if __name__ == '__main__':
    from components.config.logsmanager import logger;
    from components.property_manager import get_property_value

    logger.info("current env "+ str(get_property_value("url.phman")))

