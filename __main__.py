
if __name__ == '__main__':
    from components.config.logsmanager import logger;
    from components.property_manager import get_property_value
    from components.utils.file_util import get_path


    print('LS'+get_path(__file__))
    logger.info("current env "+ str(get_property_value("url.phman")))

