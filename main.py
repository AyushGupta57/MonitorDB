# import the required modules
import requests
from bs4 import BeautifulSoup

# Loop continuously
while True:
    # Send a GET request to the Amazon India website
    request = requests.get("https://www.amazon.in/s?k=monitors")

    # Check if the request was successful (status code 200)
    if request.status_code == 200:
        # Get the HTML content of the webpage
        html = request.content

        # Create a BeautifulSoup object with the HTML content and parse it
        soup = BeautifulSoup(html, "html.parser")

        # Find the first link with class "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"
        a_href = soup.find("a", {"class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"}).get('href')

        # Print the href attribute of the link
        print(a_href)

        # Exit the loop
        break
