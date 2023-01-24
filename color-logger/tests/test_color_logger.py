import sys
import logging
from color_logger import ColorLogger


logger = ColorLogger.get_logger(__name__, level=logging.DEBUG, output_stream=sys.stdout)

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
