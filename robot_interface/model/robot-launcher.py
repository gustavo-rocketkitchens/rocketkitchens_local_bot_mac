import os

# #  To run With Script
# from rocket_kitchens.Admin import admin as ad
# from rocket_kitchens_local_bot.robot_interface.model.parameters import Parameters
# from rocket_kitchens_local_bot.robot_interface.model.robot_models.Zoey import zoey

#  To run in Pyinstaller
from parameters import Parameters
from robot_models.Sal import sal
from robot_models.Leo import leo
from robot_models.Leo import marketing_analysis
from robot_models.Zoey import zoey
from robot_models import admin as ad
import tabalat_search




class RobotLauncher:


    def __init__(self):

        print("RobotLauncher Class")

        self.enter_talabat = 'Enter Talabat'
        self.extract_orders = 'Extract Orders'
        self.extract_reports = ''
        self.exit_talabat = ''
        self.zoey = 'Zoey'
        self.leo = 'Leo'
        self.leo_marketing_analysis = 'Leo-MarketingAnalysis'

        self.sal = 'Sal'

        #===============================================================
        # Launch the following Robots:
        #===============================================================

        # Zoey

        self.bot_zoey = zoey.Start  # Instantiate but not start

        # Leo

        self.bot_leo = leo.Start  # Instantiate but not start


        # Leo Marketing Analysis

        self.bot_leo_mkt = marketing_analysis.Start  # Instantiate but not start

        # Sal

        self.bot_sal = sal.Start  # Instantiate but not start

    def get_parameters(self):
        # Navigate to the required folder
        src_path = os.path.join(os.path.expanduser("~"), "Downloads", "output")

        filename = 'File.csv'
        filepath = os.path.join(src_path, filename)
        params = Parameters(filepath)

        # Get the first row of the dataframe
        row = params.df.iloc[0]

        # Extract the first value in the first cell of the row
        parameter = row.iloc[0]

        # Get the row for the extracted parameter
        self.variable_name, values = params.get_row(parameter)

        # Print the variable name and values to verify that they have been assigned correctly
        print(f'robot-launcher function name: {self.variable_name} \n in get_parameters')
        print(f'Variable name: {self.variable_name}')
        print(f'Values: {values}')

    def start_robots(self):
        match self.variable_name:

            case self.zoey:
                self.bot_zoey().zoey_process()  # Start robot  with zoey parameters
            case self.leo:
                self.bot_leo().leo_process()
            case self.leo_marketing_analysis:
                self.bot_leo_mkt().leo_process()
            case self.sal:
                self.bot_sal().sal_process()
            case _:
                print("Invalid variable name")


if __name__ == "__main__":
    rl = RobotLauncher()
    rl.get_parameters()
    rl.start_robots()


