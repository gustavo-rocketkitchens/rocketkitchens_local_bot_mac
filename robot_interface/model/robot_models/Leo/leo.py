import os

import rpa as r
import json
import requests
import logging
# from leo_core import TaskAutomator, HandlerSheet
from robot_models.Leo.leo_core import TaskAutomator, HandlerSheet

# from rocket_kitchens.Admin import orders_execution_post

# =======================================================================================================================

# Local Bot
from robot_models import orders_execution_post as post
from parameters import Parameters

# =======================================================================================================================

# Felicidade PC
# from rocket_kitchens_local_bot.robot_interface.model.robot_models  import orders_execution_post as post
# from rocket_kitchens_local_bot.robot_interface.model.parameters import Parameters

# =======================================================================================================================

# Notebook
# from robot_interface.model.robot_models import orders_execution_post as post
# from robot_interface.model.parameters import Parameters


# =======================================================================================================================


class Start:


    def __init__(self):
        self.sales = None
        self.total = None
        self.dish = None
        self.gross_profit = None
        self.avg_comission = None
        self.sum_food_values = None
        self.sum_discount_values = None
        logging.info("Initializers")
        logging.info("Task Automator Class")
        self.bot = TaskAutomator()
        self.handler = HandlerSheet()

    def get_parameters(self):
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
        logging.info(f'robot-launcher function name: {self.variable_name} \n in zoey.py')
        logging.info(f'Variable name: {self.variable_name}')
        logging.info(f'Values: {values}')

        self.username, self.password = params.get_pass(self.variable_name)

        # Print the username and password to verify that they have been assigned correctly
        logging.info(f'Username: {self.username}')
        logging.info(f'Password: {self.password}')
        return self.username, self.password

    def leo_reports_menu_item(self):
        # =======================================
        #     Leo   execution: Report 1 (items analysis)
        # You get the report from Talabat > reports > sales per menu items
        # =======================================
        #
        logging.info("leo_reports_menu_item instance: \n self.username, self.password = self.get_parameters() ")
        self.username, self.password = self.get_parameters()
        self.bot.enter_talabat(username=self.username, password=self.password)
        r.wait(12)
        self.bot.talabat_sales_per_menu_item()
        # r.wait(4)
        # self.bot.talabat_sales_per_area()
        r.wait(4)
        self.bot.exit_talabat()
        r.wait(2)
        self.bot.talabat_close_page()
        self.bot.tab_time()

    def leo_file_handler(self):

        logging.info('start leo file handler')

        # ---------------------------
        # Start File Handler
        # ---------------------------

        # r.wait(2)
        self.handler.talabat_read_menu_item()
        r.wait(2)
        self.dish, self.total, self.sales = self.handler.talabat_menu_item_params()
        r.wait(2)
        self.handler.delete_output_file("File.csv")
        logging.info("successfully delete output file")

    def leo_post(self):

        logging.info('start leo post')

        # ---------------------------
        # POST with orders_execution_post
        # ---------------------------

        logging.info('self.dish, self.total, self.sales')
        logging.info(self.dish, self.total, self.sales)

        # Now we post request the robots output values
        post.post_request(sum_discount_values=None,
                          sum_food_values=None,
                          avg_comission=None,
                          gross_profit=None,
                          dish=self.dish,
                          total=self.total,
                          sales=self.sales,
                          )
        ...

    def leo_process(self):

        self.leo_reports_menu_item()
        logging.info('successfully leo reports menu item')

        self.leo_file_handler()
        logging.info('successfully leo file handler')
        self.leo_post()
        logging.info('successfully leo post')
        logging.info('successfully finished leo process')

        ...

# if __name__ == '__main__':
#     start = Start()
#     start.leo_process()




