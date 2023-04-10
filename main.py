import requests
from bs4 import BeautifulSoup

while True:
    request = requests.get("https://www.amazon.in/s?k=monitors")
    if request.status_code == 200:
        # print(request.encoding)
        html = request.content
        soup = BeautifulSoup(html, "html.parser")
        a_href = soup.find("a", {"class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"}).get('href')
        print(a_href)
        break