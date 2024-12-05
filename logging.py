import logging

## Examples of the logger class (https://docs.python.org/3/howto/logging.html) (https://realpython.com/python-logging/)

# Within a class
self.logger = logging.getLogger('SessionVisualizer')
logging.basicConfig(level=logging.INFO if verbose else logging.WARNING)

self.logger.info('inform about something')


# A very common situation is that of recording logging events in a file
logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')
logger.error('And non-ASCII stuff, too, like Øresund and Malmö')

## Inspired in BERTopic logger
class MyLogger:
    def __init__(self):
        self.logger = logging.getLogger("BERTopic")

    def configure(self, level):
        self.set_level(level)
        self._add_handler()
        self.logger.propagate = False

    def info(self, message):
        self.logger.info(f"{message}")

    def warning(self, message):
        self.logger.warning(f"WARNING: {message}")

    def set_level(self, level):
        levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if level in levels:
            self.logger.setLevel(level)

    def _add_handler(self):
        sh = logging.StreamHandler()
        sh.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(message)s"))
        self.logger.addHandler(sh)

        # Remove duplicate handlers
        if len(self.logger.handlers) > 1:
            self.logger.handlers = [self.logger.handlers[0]]
