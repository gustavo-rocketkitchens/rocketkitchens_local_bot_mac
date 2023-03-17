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
from talabat_search_marketing_analysis import MarketingAnalysis
from request_app import GetMenuItem
# =======================================================================================================================

# Felicidade PC
# from rocket_kitchens_local_bot.robot_interface.model.robot_models  import orders_execution_post as post
# from rocket_kitchens_local_bot.robot_interface.model.parameters import Parameters

# =======================================================================================================================

# Notebook
# from robot_interface.model.robot_models import orders_execution_post as post
# from robot_interface.model.parameters import Parameters


# =======================================================================================================================
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('app.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

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


    def leo_marketing_analysis(self):
        self.mkt = MarketingAnalysis()
        self.area = 'Business Bay'
        self.cuisine = 'Pizza'
        logger.info(f"Getting details for restaurants in {self.area} serving {self.cuisine} cuisine")
        self.url = self.mkt.input_area(self.area)

        self.mkt.input_cuisine(self.cuisine, self.url)
        logger.info(f"Finished retrieving restaurant details for {self.cuisine} cuisine in {self.url}")
        # # time.sleep(10)
        restaurants = self.mkt.output_restaurants_url(self.cuisine, self.url)
        logger.info(f"Finished retrieving restaurant URL's for {self.cuisine}")
        # #
        # time.sleep(2)
        logger.info(f"Getting Menu Category Info for restaurants in {self.area} serving {self.cuisine} cuisine")
        self.mkt.get_menu_categories(restaurants)
        #
        # mkt.output_menu_item(url)
        # logger.info("Completed scraping menu items and writing to CSV file.")
        #

        ...

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

        self.leo_marketing_analysis()
        logging.info('successfully Marketing Analysis Extraction')

        # self.leo_file_handler()
        # logging.info('successfully leo file handler')
        # self.leo_post()
        # logging.info('successfully leo post')
        logging.info('successfully finished Marketing Analysis process')

        ...

# if __name__ == '__main__':
#     start = Start()
#     start.leo_process()




