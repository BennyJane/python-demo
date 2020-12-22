import os
import sys
import time
import logging
from colorama import Fore
from logging.handlers import TimedRotatingFileHandler

from .config import logConfig

loggers = {}


def setLogger(name=None):
    """
    get logger by name
    :param name: name of logger
    :return:
    """
    global loggers
    if not name: name = __name__

    if loggers.get(name):
        return loggers.get(name)

    logger = logging.getLogger(name)
    logger.setLevel(logConfig.LOG_LEVEL)

    # 输出到控制台
    if logConfig.LOG_ENABLED and logConfig.LOG_TO_CONSOLE:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(level=logConfig.LOG_LEVEL)
        formatter = logging.Formatter(logConfig.LOG_FORMAT)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    if logConfig.LOG_ENABLED and logConfig.LOG_TO_FILE:
        # 如果路径不存在, 则创建日志文件夹
        nowTime = time.strftime("%Y-%m-%d")
        LOG_PATH = logConfig.LOG_PATH + '/' + nowTime + '.log'
        # LOG_PATH = logConfig.LOG_PATH + '/demo.log'
        log_dir = os.path.dirname(LOG_PATH)
        if not os.path.exists(log_dir): os.makedirs(log_dir)  # 需要创建路径与相应的文件

        file_handler = TimedRotatingFileHandler(LOG_PATH, when='m', backupCount=3, encoding='utf-8')
        file_handler.setLevel(level=logConfig.LOG_LEVEL)
        formatter = logging.Formatter(logConfig.LOG_FORMAT)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    loggers[name] = logger
    return logger


class customLog:
    def __init__(self, name):
        self.logger = setLogger(name)

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(
            Fore.YELLOW + msg + Fore.RESET
        )

    def error(self, msg):
        self.logger.error(
            Fore.RED + msg + Fore.RESET
        )

    def warning(self, msg):
        self.logger.warning(
            Fore.LIGHTYELLOW_EX + msg + Fore.RESET
        )


logger = customLog("custom")
