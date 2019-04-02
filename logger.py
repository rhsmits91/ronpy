import logging

# set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s',
                    datefmt='%m-%d %H:%M')

# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)

# add the handler to the root logger
logger = logging.getLogger('sainsburys')
logger.addHandler(console)
