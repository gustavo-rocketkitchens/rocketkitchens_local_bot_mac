

import requests
from bs4 import BeautifulSoup
from request_app import GetMenuItem
import pandas as pd


class URLParser:
    def __init__(self):
        self.get_item = GetMenuItem()
        self.area_list = self.get_item.area
        self.cities = ['dubai', 'abu-dhabi', 'sharjah']  # list of cities to remove from url

    def url_parser(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        valid_areas = []
        for link in links:
            for area in self.area_list:
                if area.lower() in link.text.lower():
                    if any(city in link['href'].lower() for city in self.cities):
                        print(f"{area} found in {link['href']}, but has a city in the path and is invalid")
                    elif "restaurants" not in link['href'].lower():
                        print(
                            f"{area} found in {link['href']}, but doesn't contain 'restaurants' in the path and is invalid")
                    else:
                        print(f"{area} found in {link['href']} and is valid")
                        valid_areas.append(link['href'])
                    break
            else:
                continue
            break
        else:
            print(f"No areas found in {url}")
        return valid_areas

    def get_area_url(self, area_name):
        for url in self.url_parser("https://www.talabat.com/uae/sitemap"):
            if area_name.lower() in url.lower():
                return url
        else:
            print(f"No URL found for {area_name}")
            return None


if __name__ == "__main__":
    parser = URLParser()
    area_name = "Dasman"
    url = parser.get_area_url(area_name)
    if url:
        print(f"URL for {area_name}: {url}")
    else:
        print(f"No URL found for {area_name}")

    print(f"--------------------------------")
    print(f"url? ", url)