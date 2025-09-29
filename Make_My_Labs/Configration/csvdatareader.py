import logging

import pandas as pd


class Csvdatareader:
    # @staticmethod
    # def get_data_from_csv(csv_file_path, value):
    #     """
    #     Static method to read a CSV file and find a specific value in one of its columns.
    #
    #     Parameters:
    #     CSV_file_path (str): The path to the CSV file.
    #     Value (str): The value to search for in the CSV file.
    #
    #     Returns:
    #     str: The corresponding content of cell if the value is found.
    #
    #     Raises:
    #     ValueError: If the value is not found in the CSV file.
    #     FileNotFoundError: If the CSV file does not exist.
    #     Exception: For any other exceptions that occur during the process.
    #     """
    #     try:
    #         # Read the CSV file into a DataFrame
    #         df = pd.read_csv(csv_file_path)
    #         # Convert the entire DataFrame (excluding headers) to a list of lists
    #         data_list = df.values.tolist()
    #
    #         # Filter the list to find the sublist containing the specified Value
    #         filtered_list = [row for row in data_list if value in row]
    #
    #         # Check if the filtered list is not empty
    #         if filtered_list:
    #             # Get the first matching row
    #             matching_row = filtered_list[0]
    #             # Extract the content of cell (assuming it is the last element in the row)
    #             content = matching_row[-1]
    #             return content
    #         else:
    #             # Raise an exception if the value is not found in any row
    #             raise ValueError("Value not found")
    #     except FileNotFoundError:
    #         # Handle the case where the CSV file does not exist
    #         logging.info("CSV file not found.")
    #     except Exception as e:
    #         # Handle any other exceptions that occur
    #         logging.info("An error occurred: %s", e)
    #         # Optionally raise the exception to propagate it further
    #         raise
    @staticmethod
    def get_data_from_csv(csv_file_path, value, column_name):
        """
        Static method to read a CSV file and find a specific value in one of its columns, returning the value
        from a specified column in the matching row.

        Parameters:
        csv_file_path (str): The path to the CSV file.
        value (str): The value to search for in the CSV file.
        column_name (str): The name of the column from which to retrieve the value in the matching row.

        Returns:
        str: The corresponding content of the specified column if the value is found.

        Raises:
        ValueError: If the value is not found in the CSV file.
        FileNotFoundError: If the CSV file does not exist.
        Exception: For any other exceptions that occur during the process.
        """
        try:
            # Read the CSV file into a DataFrame
            df = pd.read_csv(csv_file_path)

            # Check if the value is in any row of the DataFrame
            if value in df.values:
                # Find the row where the value is located
                matching_row = df[df.isin([value]).any(axis=1)].iloc[0]

                # Return the value from the specified column
                return matching_row[column_name]
            else:
                # Raise an exception if the value is not found in any row
                raise ValueError("Value not found")
        except FileNotFoundError:
            # Handle the case where the CSV file does not exist
            logging.info("CSV file not found.")
            raise
        except Exception as e:
            # Handle any other exceptions that occur
            logging.info("An error occurred: %s", e)
            raise
