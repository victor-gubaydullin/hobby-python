import os
import logging
from config import load_config

config = load_config()

def setup_logging(log_name, log_level=logging.INFO):
    log_dir = config.LOG_DIR
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger(log_name)
    logger.setLevel(logging.INFO)

    file_formatter = logging.Formatter(
        fmt='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    stream_formatter = logging.Formatter(
        fmt='[%(name)s] %(levelname)s: %(message)s'
    )

    # Log within a file
    file_handler = logging.FileHandler(os.path.join(log_dir, f'{log_name}.log'))
    file_handler.setFormatter(file_formatter)

    # Log to console
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(stream_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger