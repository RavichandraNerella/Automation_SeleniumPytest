import configparser

from Config.config import TestData
from Utils.Logs.logger import logger

TESTS_DATA_PATH = TestData.TESTDATA_PATH
config = configparser.RawConfigParser()
config.read(TESTS_DATA_PATH)


class TestBase:
    # read tests data .ini file and return the desired property
    @staticmethod
    def get_data(prop):
        try:
            return config.get('tests data', prop)
        except Exception:
            message = "Tests data file was not found"
            logger.exception(message)
            raise FileNotFoundError(message)


