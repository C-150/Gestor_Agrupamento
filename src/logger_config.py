# logger_config.py

import logging

def configurar_logger():
    logger = logging.getLogger()  # root logger

    if logger.handlers:  # evita duplicar handlers
        return logger

    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler("app.log", encoding="utf-8")
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(module)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger

app_logger = configurar_logger()