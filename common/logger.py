'Common Logger'

import sys
import logging

# standardise all logging
class CommonLogger():
    """
    Class to call for standardising logging output with convenience functions:
    log_<logging level>(msg, to_screen=True)
        log msg with the named logging level. Print to screen or not.
    """
    __instance = None

    def __init__(self):
        if CommonLogger.__instance is not None:
            raise ValueError("""CommonLogger already exists.
            Use CommonLogger.get_instance() to get or create the singleton.
            """)
        else:
            CommonLogger.__instance = self
        # standardise all logging of processes
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        logger = logging.getLogger('copywriter-api')
        logger.addHandler(stream_handler)
        logger.setLevel(logging.INFO)

        self.logger = logger

    @staticmethod
    def get_instance():
        'Access the Singleton'
        if CommonLogger.__instance is None:
            CommonLogger()
        return CommonLogger.__instance

    def log(self, level, msg):
        '''
        '''
        level_switch = {"debug" : self.logger.debug,
                        "info" : self.logger.info,
                        "warning" : self.logger.warning,
                        "error" : self.logger.error
                        }
        level_switch[level](msg)
    def log_debug(self, msg):
        self.log("debug", msg)
    def log_info(self, msg):
        self.log("info", msg)
    def log_warning(self, msg):
        self.log("warning", msg)
    def log_error(self, msg, raise_error=False, type_of_exception=None):
        self.log("error", msg)
        if raise_error:
            if type_of_exception:
                raise type_of_exception(msg)
            else:
                raise RuntimeError(msg)