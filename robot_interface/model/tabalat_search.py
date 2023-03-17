import os
import rpa as r
import json
import ast
import requests
from bs4 import BeautifulSoup
from bs4.element import Comment


import logging
import time
# from leo_core import TaskAutomator, HandlerSheet
from robot_models.Leo.leo_core import TaskAutomator, HandlerSheet
import csv
# from rocket_kitchens.Admin import orders_execution_post

# =======================================================================================================================

# Local Bot
from robot_models import orders_execution_post as post
from parameters import Parameters

# =======================================================================================================================
from foreground_model import get_page_title, activate_window


class TalabatSearch:


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tab_log = float()






        ...

    def talabat_search(self):

        url = r"https://www.talabat.com/uae"

        # Configure logging
        logger = logging.getLogger(__name__)

        # get the start time
        st = time.time()

        r.init(visual_automation=True)
        # title = get_page_title(url)

        # focus = "focus(title='{}')".format(title)
        # maximize = "maximize (title='{}')".format(title)
        # r.run(focus)
        # r.run(maximize)
        r.url(url)
        r.wait(1)
        #
        # r.run(focus)
        # r.run(maximize)
        # activate_window(title)
        # r.wait(1)
        # r.run(maximize)
        # logger.info("Maximizing")
        r.keyboard("[alt][space]")
        r.keyboard("x")
        r.wait(1)
        logger.info("Maximizing Screen")
        r.keyboard("[alt][space]")
        r.keyboard("x")

        # Search
        r.wait(2)
        # r.type("//input[@id='search-box-map-first']", "Sushi")
        r.type("//input[@id='search-box-map-first']", "[clear]" + "Business Bay, Marasi Drive")

        r.wait(.2)
        r.click("//button[@data-testid='letsgo-btn']")
        r.wait(2)

        logger.info("Restaurants in Business Bay for delivery")
        r.type("//input[@placeholder='Search Restaurants']", "Sushi[enter]")
        r.wait(.2)
        # r.type("//input[@id='placeSearch']", "Business Bay - Dubai")
        # r.wait(.2)
        r.click("/html[1]/body[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/a[1]/div[1]")

        # get the end time
        et = time.time()

        # get the execution time
        elapsed_time = et - st
        logger.info('Log in Tabalat execution time: %s seconds', elapsed_time)

        self.tab_log = elapsed_time


    def talabat_menu_item(self):

        logger = logging.getLogger(__name__)

        logger.info("catalog screen")
        r.click("//body/div[@id='__next']/div/div/div[@data-test='catalogue-screen']/div/div/div/div/div[2]/div[1]/div[1]/div[2]/div[1]")

        logger.info("First Menu Category")
        # r.click("//body/div[@id='__next']/div/div/div[@data-test='catalogue-screen']/div/div/div/div/div/div/div/div[1]/div[2]/div[1]")
        r.click("//body/div[@id='__next']/div/div/div[@data-test='catalogue-screen']/div/div/div/div/div/div/div/div[1]/div[2]/div[1]")

        logger.info("Menu Item")
        name = r.read("//body//div[@id='__next']//div[@data-test='catalogue-screen']//div//div//div//div//div//div//div//div[1]//div[1]//div[2]//div[1]//div[1]//div[2]//div[1]")
        # r.click("")
        logger.info(name)

        ...


    @staticmethod
    def talabat_close_page():

        r.keyboard("[alt][F4]")
        r.wait(1)


    #========================================
    @staticmethod
    def get_html(url, output_folder):
        logger = logging.getLogger(__name__)
        logger.info("Fetching HTML from URL: %s", url)

        response = requests.get(url)
        logger.info("Got response with status code %d", response.status_code)

        soup = BeautifulSoup(response.text, 'html.parser')
        logger.info("Parsed HTML content")

        # Divide the HTML content into 10 parts
        num_parts = 10
        content_len = len(str(soup))
        part_len = content_len // num_parts

        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Write each part to a separate file
        for i in range(num_parts):
            start_idx = i * part_len
            end_idx = (i + 1) * part_len
            if i == num_parts - 1:
                # For the last part, include the remaining content
                end_idx = content_len
            part_content = str(soup)[start_idx:end_idx]
            filename = os.path.join(output_folder, f"{i + 1:02}-file.txt")
            with open(filename, "w", encoding="utf-8") as f:
                f.write(part_content)
            logger.info("Wrote part %d to file %s", i + 1, filename)

        return soup

    def clean_html(self, file_path):
        # Read the HTML content from the file with utf-8-sig encoding
        with open(file_path, encoding="utf-8-sig") as f:
            content = f.read()

        # Replace any commas with dots in the HTML content
        content = content.replace(',', '.')

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(content, "html.parser")

        # Remove any script tags
        for script in soup.find_all("script"):
            script.extract()

        # Remove any style tags
        for style in soup.find_all("style"):
            style.extract()

        # Remove any comments
        for comment in soup.find_all(text=lambda text: isinstance(text, Comment)):
            comment.extract()

        # Remove any empty tags
        for tag in soup.find_all():
            if not tag.contents:
                tag.extract()

        # Convert the modified HTML content back to a string
        cleaned_content = str(soup)

        return cleaned_content
    # ========================================

if __name__ == '__main__':
    TS = TalabatSearch()
    TS.talabat_search()
    time.sleep(3)
    TS.talabat_menu_item()
    # TS.talabat_close_page()
