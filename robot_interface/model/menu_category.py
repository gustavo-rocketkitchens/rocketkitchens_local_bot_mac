import logging
import csv
import time
from playwright.sync_api import Playwright, sync_playwright

# Configure logging
logging.basicConfig(level=logging.INFO)


def scrape_menu_items(url: str) -> dict:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)

        # Get a list of all menu category elements
        menu_categories = page.query_selector_all("[data-test='menu-category']")
        logging.info(f"Found {len(menu_categories)} menu categories")

        menu_items = {}

        for category_index in range(1, len(menu_categories)+1):
            # Get the menu category name
            category_name = page.inner_text(f"(//div[@data-test='menu-category'])[{category_index}]", timeout=60000)
            logging.info(f"Scraping category {category_name}")

            # Get the list of menu item names and prices
            item_names = page.inner_text(f"(//div[@data-test='menu-category'])[{category_index}]//div[@class='item-name']")
            item_prices = page.inner_text(f"(//div[@data-test='menu-category'])[{category_index}]//div[@class='text-right price-rating']")

            # Split the list of names and prices into individual items
            item_names = item_names.split('\n')
            item_prices = item_prices.split('\n')

            # Create a dictionary of menu items for this category
            category_items = {}
            for i in range(len(item_names)):
                # If the number of names and prices are not equal, use an empty string for the missing value
                category_items[item_names[i].strip()] = item_prices[i].strip() if i < len(item_prices) else ''

            # Add the category items to the menu_items dictionary
            menu_items[category_name] = category_items

            # Delay to avoid overcharging
            time.sleep(0.1)

        browser.close()

        return menu_items


def write_menu_items_to_csv(menu_items: dict, filename: str):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Category', 'Item', 'Price'])
        for category_name, category_items in menu_items.items():
            for item_name, item_price in category_items.items():
                writer.writerow([category_name, item_name, item_price])


#if __name__ == '__main__':
#     url = "https://www.talabat.com/uae/restaurant/619284/manzo-sushi-and-sliders-khalifa-city-madinat-khalifa--a?aid=2060"
#     menu_items = scrape_menu_items(url)
#     print(menu_items)
#     # write_menu_items_to_csv(menu_items, 'menu_items.csv')
