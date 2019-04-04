import logging

def setup_ronpy_logging_config():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(name)-12s %(levelname)-8s',
                        datefmt='%m-%d %H:%M')

# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)

# add the handler to the root logger
logger = logging.getLogger(__package__)
logger.addHandler(console)
