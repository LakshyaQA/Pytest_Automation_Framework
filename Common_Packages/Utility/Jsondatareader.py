import json


class Jsondatareader:
    @staticmethod
    def get_data_from_json(json_file_path, array_name):
        """
        Reads a specific array from a JSON file containing multiple arrays.

        Parameters:
        JSON_file_path (str): The path to the JSON file.
        array_name (str): The name of the array to read.

        Returns:
        list: A list of dictionaries, each containing values from the specified array.
        If the array name is not found, returns an empty list.
        """
        # Open the JSON file for reading
        with open(json_file_path, 'r') as json_file:
            # Load the JSON data into a Python dictionary
            data = json.load(json_file)
            values_list = []  # Initialize an empty list to store extracted values
            # Check if the array name exists in the JSON data
            if array_name in data:
                array_data = data[array_name]  # Get the array data
                # Iterate over each dictionary in the array
                for d in array_data:
                    # Extract values from the dictionary and convert them to a list
                    values_list.append(list(d.values()))
                return values_list  # Return the list of values extracted from the array
            else:
                return []  # If the array name is not found, return an empty list
