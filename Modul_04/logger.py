import logging
from functools import wraps


def logged(level, name=None, message=None):
    def decorate(func):
        log_name = name if name else func.__module__
        log_message = message if message else func.__name__
        logger = logging.getLogger(log_name)
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            logger.log(level, log_message)
            return result
        return wrapper
    return decorate

