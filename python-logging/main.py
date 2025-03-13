import atexit
import logging
import logging.config
import json

'''
https://github.com/mCodingLLC/VideosSampleCode/tree/master/videos/135_modern_logging
'''

logger = logging.getLogger("main") # or __name__

def setup_logging():
    with open('logging_config.json', 'r') as f:
        config = json.load(f)
    logging.config.dictConfig(config)
    queue_handler = logging.getHandlerByName('queue_handler')
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)


def main():
    setup_logging()
    logging.basicConfig(level="INFO")
    logger.debug("debug message", extra={"x": "hello"})
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
    try:
        1 / 0
    except ZeroDivisionError as e :
        logger.exception(f"exception message: {e}")


if __name__ == '__main__':
    for _ in range(1_000):
        main()