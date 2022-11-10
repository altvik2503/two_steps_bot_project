from pathlib import Path
import sys

BASE_DIR = Path.cwd().parent
CODE_DIR_PATH = BASE_DIR / 'two_steps_bot'
sys.path.append(str(CODE_DIR_PATH))

STATIC = 'static'

TOKEN = '5673765058:AAHjhehxRV-U79KjntGh3laCpoGaG1A6-Cw'

DEBUG = True

# logging
LOGGIN_LEVEL = 'DEBUG' if DEBUG else 'INFO'
APP_FORMAT = '[%(asctime)s] [%(levelname)s] > %(message)s'
ERR_FORMAT = (
    '[%(asctime)s] [%(name)s] [%(levelname)s]'
    ' (%(filename)s).(%(funcName)s)(%(lineno)d) > %(message)s'
)
LOGIT_FORMAT = '[%(asctime)s] [%(name)s] [%(levelname)s] > %(message)s'
LOGGIN_DATEFMT = '%d-%b-%y %H:%M:%S'

LOCAL_LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'app_formatter': {
            'format': APP_FORMAT,
            'datefmt': LOGGIN_DATEFMT,
        },
        'err_formatter': {
            'format': ERR_FORMAT,
            'datefmt': LOGGIN_DATEFMT,
        },
        'logit_formatter': {
            'format': LOGIT_FORMAT,
            'datefmt': LOGGIN_DATEFMT,
        },
    },

    'handlers': {
        'app_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'app_formatter',
        },
        'err_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'err_formatter',
        },
        'logit_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'logit_formatter',
        },
    },

    'loggers': {
        'app_logger': {
            'handlers': ['app_handler'],
            'level': LOGGIN_LEVEL,
            'propagate': True
        },
        'err_logger': {
            'handlers': ['err_handler'],
            'level': LOGGIN_LEVEL,
            'propagate': True
        },
        'logit_logger': {
            'handlers': ['logit_handler'],
            'level': 'DEBUG',
            'propagate': True
        },
    },
}
