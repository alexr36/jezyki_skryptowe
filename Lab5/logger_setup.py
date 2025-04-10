# === Globally used logger =====================================================
# - Logs of levels: INFO, DEBUG, WARNING  --> stdout
# - Logs of levels: ERROR, CRITICAL       --> stderr
# ==============================================================================

import logging, sys


logger = logging.getLogger('cli_logger')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("[%(levelname)s] %(message)s")

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.addFilter(lambda record: record.levelno <= logging.WARNING)
stdout_handler.setFormatter(formatter)
logger.addHandler(stdout_handler)

stderr_handler = logging.StreamHandler(sys.stderr)
stderr_handler.setLevel(logging.ERROR)
stderr_handler.setFormatter(formatter)
logger.addHandler(stderr_handler)

# Defined logger object is the only importable element
__all__ = ['logger']