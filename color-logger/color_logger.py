import logging
import sys
from colorama import Fore, Back, Style


COLOR_MAP = {
    'DEBUG':    Fore.CYAN,
    'INFO':     Fore.GREEN,
    'WARNING':  Fore.YELLOW,
    'ERROR':    Fore.RED,
    'CRITICAL': Fore.RED + Back.WHITE
};


class ColorFormatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None, style='{'):
        super().__init__(fmt, datefmt, style)

    def format(self, record):
        levelname = record.levelname
        if levelname in COLOR_MAP:
            record.levelname = COLOR_MAP[levelname] + levelname + Style.RESET_ALL
        return super().format(record)



class ColorLogger:
    @staticmethod
    def get_logger(name, level=logging.INFO, output_stream=sys.stdout):
        logger = logging.getLogger(name)
        logger.setLevel(level)
        formatter = ColorFormatter("{asctime} [{levelname:^20}] {message}")
        formatter.datefmt = "%Y-%m-%d %H:%M:%S"
        stream_handler = logging.StreamHandler(output_stream)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
        return logger