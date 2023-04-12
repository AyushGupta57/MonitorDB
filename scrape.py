# Import the necessary libraries
import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp

def Scraper():
    # Initialize empty lists to store monitor names, links, and prices
    monitor_name_raw = list()
    monitor_name = list()
    monitor_link = list()
    monitor_price_raw = list()
    monitor_price = list()

    # Initialize the page number and a flag for checking if there are more pages to scrape
    page = 1
    next_page = True

    # Loop through the pages of search results until there are no more pages
    while next_page:

        # Construct the URL for the Amazon search results page for monitors
        url = "https://www.amazon.in/s?k=monitors&page=" + str(page)

        # Send a GET request to the URL
        request = requests.get(url)

        # Check if the request was successful
        if request.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            html = request.content
            soup = BeautifulSoup(html, "html.parser")

            # Find all monitor product links on the page and store them in monitor_hrefs list
            for a_href in soup.find_all("a", {"class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"}):
                link = "https://www.amazon.in" + a_href.get('href')
                monitor_link.append(link)

            # Find all monitor names on the page and store them in monitor_names list
            for names in soup.find_all("span", {"class": "a-size-medium a-color-base a-text-normal"}):
                monitor_name_raw.append(names.text)

            # Find all monitor prices on the page and store them in monitor_price list
            for prices in soup.find_all("span", {"class": "a-price-whole"}):
                monitor_price_raw.append(prices.text)

            # Check if there is a "next page" button on the page; if not, exit the loop
            next_button = soup.find("span", {"class": "s-pagination-item s-pagination-next s-pagination-disabled"})
            if next_button != None:
                next_page = False
            else:
                page = page + 1

    # print(monitor_hrefs)
    # print(monitor_names)
    # print(monitor_price)

    # Remove comma from monitor_price_comma list and convert string to float with 2 decimal places
    monitor_price = ["{:.2f}".format(float(x.replace(",", ""))) for x in monitor_price_raw]

    # Change ' to \' in monitor_names_raw list
    monitor_name = [x.replace("'", "\'") for x in monitor_name_raw]
    
    # Print the scraped monitor names, prices, and links using the pprint library
    return list(zip(monitor_name, monitor_price, monitor_link))

# pp(Scraper())