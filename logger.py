import logging

logger = logging.getLogger(__name__)

# the handler determines where the logs go: stdout/file
handler = logging.StreamHandler()

# the formatter determines what your logs will look like
fmt = "%(asctime)s %(levelname)s [%(filename)s:%(lineno)s] %(message)s"
formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)

logger.addHandler(handler)
# levels DEBUG, INFO, WARNING, ERROR, CRITICAL
logger.setLevel(logging.DEBUG)

logger.debug("Debug prompt")
logger.info("Info only")
logger.warning("This is a warning")
logger.error("another error")
logger.critical("Critical issue!")
