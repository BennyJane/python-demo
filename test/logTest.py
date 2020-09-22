from loggerSetting.logSetting import setLogger, logger
import time


# logger = setLogger("demo")

def base():
    while True:
        time.sleep(5)
        logger.info("pass word!!")
        logger.debug("1111111 pass word!!")
        logger.error("2222222 pass word!!")


base()
