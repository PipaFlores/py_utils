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
