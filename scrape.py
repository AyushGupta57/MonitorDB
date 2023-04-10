# Import the necessary libraries
import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp

# Initialize empty lists to store monitor names, links, and prices
monitor_names = list()
monitor_link = list()
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
            monitor_names.append(names.text)

        # Find all monitor prices on the page and store them in monitor_price list
        for prices in soup.find_all("span", {"class": "a-price-whole"}):
            monitor_price.append(prices.text)

         # Check if there is a "next page" button on the page; if not, exit the loop
        next_button = soup.find("span", {"class": "s-pagination-item s-pagination-next s-pagination-disabled"})
        if next_button != None:
            next_page = False
        else:
            page = page + 1

# print(monitor_hrefs)
# print(monitor_names)
# print(monitor_price)

# Print the scraped monitor names, prices, and links using the pprint library
for name, price, link in list(zip(monitor_names, monitor_price, monitor_link)):
    pp(f"{name} {price} {link}")