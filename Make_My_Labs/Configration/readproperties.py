import configparser
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
config = configparser.RawConfigParser()
property = configparser.RawConfigParser()
test = str(BASE_DIR)
config.read(test + "//Configration//config.ini")


class Readconfig:

    @staticmethod
    def get_username(section, opt):
        username = config.get(section, opt)
        return username

    @staticmethod
    def get_password(section, opt):
        password = config.get(section, opt)
        return password
