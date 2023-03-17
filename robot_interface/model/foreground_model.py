import logging
import pygetwindow as gw
import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)

def get_page_title(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the title of the page
    title = soup.find("title").string

    logging.info(f"Page title: {title}")

    return title

def activate_window(title):
    # Find the window with the title
    windows = gw.getWindowsWithTitle(title)
    if len(windows) > 0:
        window = windows[0]
        # Bring the window to the foreground
        window.activate()
        logging.info(f"Activated window with title: {title}")
    else:
        logging.info(f"No window found with title: {title}")

# if __name__ == "__main__":
#     title = get_page_title("https://talabat.portal.restaurant/dashboard")
#
#     activate_window(title)

