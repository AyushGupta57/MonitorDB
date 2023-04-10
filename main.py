import requests
from bs4 import BeautifulSoup

monitor_names = list()
monitor_hrefs = list()
monitor_price = list()

page = 1

while True:

    url = "https://www.amazon.in/s?k=monitors&page=" + str(page)
    request = requests.get(url)

    if request.status_code == 200:

        html = request.content

        soup = BeautifulSoup(html, "html.parser")

        for a_href in soup.find_all("a", {"class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"}):
            monitor_hrefs.append(a_href.get('href'))

        for names in soup.find_all("span", {"class": "a-size-medium a-color-base a-text-normal"}):
            monitor_names.append(names.text)

        for prices in soup.find_all("span", {"class": "a-price-whole"}):
            monitor_price.append(prices.text)

        print(monitor_hrefs)
        print(monitor_names)
        print(monitor_price)

        break
