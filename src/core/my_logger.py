import os
import logging
import logging.handlers


def set_logger(module_name):
    logger = logging.getLogger(module_name)
    logger.handlers.clear()
    logger.propagate = False

    log_level_env = os.getenv("LogLevel", "DEBUG").upper()
    log_level = logging.DEBUG if log_level_env == "DEBUG" else logging.INFO

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] (%(filename)s | %(funcName)s | l%(lineno)s) %(message)s"
    )

    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    streamHandler.setLevel(log_level)

    logger.setLevel(log_level)
    logger.addHandler(streamHandler)

    if log_level_env == "DEBUG":
        fileHandler = logging.handlers.RotatingFileHandler(
            "/tmp/api.log",
            maxBytes=10**6,
            backupCount=5,
        )
        fileHandler.setFormatter(formatter)
        fileHandler.setLevel(log_level)
        logger.addHandler(fileHandler)

    return logger


if __name__ == "__main__":
    logger = set_logger(__name__)
    logger.info("info")
    logger.debug("debug")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")
