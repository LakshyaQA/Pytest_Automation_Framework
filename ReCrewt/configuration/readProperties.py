import configparser
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
config = configparser.RawConfigParser()
property = configparser.RawConfigParser()
test = str(BASE_DIR)
config.read(test + "//configuration//configs.ini")


# config.read("C:/Users/GS-2155/PycharmProjects/pythonProject3/Configurations/logging.config")
# config.read("../Configurations/logging.config")"


class ReadConfig:
    # Methods for Dev env

    @staticmethod
    def getUsername(section, opt):
        username = config.get(section, opt)
        return username

    @staticmethod
    def getpassword(section, opt):
        password = config.get(section, opt)
        return password





