import logging

from src.logger import Logger
from src.logger.handlers import FormatterHandler

if __name__ == "__main__":
    LOG = Logger(__name__, logging.DEBUG, handlers=[FormatterHandler(logging.DEBUG)])
    LOG.debug(None, "function.input", "orchestrator", ["data"], False)
    LOG.debug(None, "function.output", "orchestrator", ["data"], False)
    LOG.error(None, "error", "orchestrator", ["data"], False)
    LOG.debug(None, "request", "orchestrator", ["data"], False)
    LOG.debug(None, "database", "orchestrator", ["data"], False)
    LOG.debug(None, None, "orchestrator", ["data"], False)
