import sys
import logging

def error_handle():
    return '{}. {}, line: {}'.format(sys.exc_info()[0],
                                           sys.exc_info()[1],
                                           sys.exc_info()[2].tb_lineno)

try:
    a+b
except Exception as e:
    # print(str(e))
    logging.error(error_handle())