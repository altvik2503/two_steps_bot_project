from logging import getLogger
import logging.config
import settings as stng

logging.config.dictConfig(stng.LOCAL_LOGGING_CONFIG)
_logger = getLogger('err_logger')


def log_errors(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as err:
            _logger.error(f'{f.__name__}: {err}')
            pass
    return inner
