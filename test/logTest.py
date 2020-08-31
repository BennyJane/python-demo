from loggerSetting.logSetting import setLogger
import time

logger = setLogger("demo")

def base():
    while True:
        time.sleep(5)
        logger.debug("pass word!!")
        logger.debug("1111111 pass word!!")
        logger.debug("2222222 pass word!!")

base()