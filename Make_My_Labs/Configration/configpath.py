import os


class UploadFile:
    @staticmethod
    def json_data_file(file_name):
        # Get the current directory of the script
        current_directory = os.path.dirname(__file__)
        # Define the JSON file name
        json_file = file_name
        # Concatenate the directory path with the JSON file name
        data_file_path = current_directory + json_file
        return data_file_path

    @staticmethod
    def csv_data_file(file_name):
        # Get the current directory of the script
        current_directory = os.path.dirname(__file__)
        # Define the csv file name
        csv_file = file_name
        # Concatenate the directory path with the csv file name
        data_file_path = current_directory + csv_file
        return data_file_path

    @staticmethod
    def file_download_location():
        current_directory = os.path.dirname(__file__)
        return current_directory
