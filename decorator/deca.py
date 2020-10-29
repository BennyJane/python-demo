import traceback
from functools import wraps

from loguru import logger


def my_logger(count):
    def step1(foo):
        @wraps(foo)
        def step2(*args, **kwargs):
            try:
                result = foo(*args, **kwargs)
                logger.info(f"{result},{count}")
            except Exception:
                logger.exception(traceback.format_exc())

        return step2

    return step1
