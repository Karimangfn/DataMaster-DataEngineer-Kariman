import os

from pythonjsonlogger import jsonlogger

#: Define the default log level from the environment variable
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

#: LOGGING_CONFIG (dict): Dictionary configuration for the Python
# logging module.
#:
#: This configuration defines:
#: - Formatters: JSON and plain-text formats.
#: - Handlers: Output to stdout using JSON formatting.
#: - Root logger and custom named logger "myapp" with customizable
# log level.
#:
#: The JSON formatter includes fields such as timestamp, logger name,
#: log level, message, module name, function name, and line number.
#:
#: The logging level can be overridden via the environment
# variable `LOG_LEVEL`.

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "()": jsonlogger.JsonFormatter,
            "fmt": (
                "%(asctime)s %(name)s %(levelname)s %(message)s "
                "%(module)s %(funcName)s %(lineno)d"
            ),
            "datefmt": "%Y-%m-%dT%H:%M:%S%z",
        },
        "simple": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "formatter": "json",
            "stream": "ext://sys.stdout",
            "level": LOG_LEVEL,
        },
    },
    "root": {
        "handlers": ["stdout"],
        "level": LOG_LEVEL,
    },
    "loggers": {
        "myapp": {
            "handlers": ["stdout"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
    },
}
