import mariadb
import logging.config
import logging
import os


class ReportModel:

    def __init__(self):
        self.current_user = []
        config_file = os.path.join(os.path.dirname(
            __file__), "config_files", "log_config.ini")
        logging.config.fileConfig(config_file)  # load logging configuration
        self.logger = logging.getLogger('sLogger')
        self.logger.debug("Creating ReportModel object")

    def connect_to_database(self):
        self.logger.debug("Connecting to database")

    def check_login(self, username, password):
        self.logger.debug("Checking login")
        current_user = []   # get infomation from database
