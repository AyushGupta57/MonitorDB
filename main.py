import requests
from bs4 import BeautifulSoup

monitor_names = list()
monitor_hrefs = list()
monitor_price = list()

page = 1

while True:

    # Construct the URL for the Amazon search results page for monitors
    url = "https://www.amazon.in/s?k=monitors&page=" + str(page)
    request = requests.get(url)

    # Check if the request was successful
    if request.status_code == 200:
        html = request.content
        soup = BeautifulSoup(html, "html.parser")

        # Find all monitor product links on the page and store them in monitor_hrefs list
        for a_href in soup.find_all("a", {"class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"}):
            monitor_hrefs.append(a_href.get('href'))

        # Find all monitor names on the page and store them in monitor_names list
        for names in soup.find_all("span", {"class": "a-size-medium a-color-base a-text-normal"}):
            monitor_names.append(names.text)

        # Find all monitor prices on the page and store them in monitor_price list
        for prices in soup.find_all("span", {"class": "a-price-whole"}):
            monitor_price.append(prices.text)

        # Print the monitor product links, names and prices
        print(monitor_hrefs)
        print(monitor_names)
        print(monitor_price)

        break  # Exit the loop once the data has been scraped from the first page

