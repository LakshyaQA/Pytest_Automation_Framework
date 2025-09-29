import configparser
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
config = configparser.RawConfigParser()
properties = configparser.RawConfigParser()
test = str(BASE_DIR)
config.read(test + "//Base//config_url.ini")
# config.read("C:/Users/GS-2155/PycharmProjects/pythonProject3/Configurations/logging.config")
# config.read("../Configurations/logging.config")"


class ReadURL:
    """ Methods for Dev env
    """

    @staticmethod
    def get_application_url(section, opt):
        """ Method to get any application URL
            """
        url = config.get(section, opt)
        return url
