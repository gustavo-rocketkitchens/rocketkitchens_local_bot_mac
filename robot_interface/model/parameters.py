import os
import pandas as pd


class Parameters:

    def __init__(self, filepath):
        self.filepath = filepath
        # Read the CSV file using pandas, specifying that the first line should be skipped
        self.df = pd.read_csv(self.filepath, header=0)

    def read_csv(self):
        # Convert the dataframe to a dictionary
        my_dict = self.df.to_dict()

        return my_dict

    def get_row(self, variable_name):
        # Get the row where the first column has the value "variable_name"
        row_values = self.df.loc[self.df[self.df.columns[0]] == variable_name].values

        # if len(row_values) == 0:
        #     return None, None

        # Assign the first cell value as the name of a variable
        variable_name = row_values[0][0]

        # Assign the rest of the cells as the values in a list
        values = row_values[0][1:]

        return variable_name, values

    def get_pass(self, variable_name):
        variable_name, values = self.get_row(variable_name)
        username = None
        password = None
        for value in values:
            if isinstance(value, str):
                username = value
                break
        if username:
            for value in values[::-1]:
                if isinstance(value, str):
                    password = value
                    break
        return username, password
