import os

class JsonPathReader:

  @staticmethod
  def path_json():
    current_directory = os.path.dirname(__file__)
    img_file = '\\ReCrewt.json'
    path = current_directory + img_file
    return path