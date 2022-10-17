import logging

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] [%(levelname)s] %(message)s in [%(module)s] -> [%(funcName)s] in [%(threadName)s]',
                    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger("main-logger")


