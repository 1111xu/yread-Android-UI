import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s %(process)d %(thread)d')

logging.debug('debug info')
logging.info('hello zxw')
logging.warning('warning info')
logging.error('error info')
logging.critical('critical info')