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

        # Create an empty list to store href links
        href_list = list()

        # Loop through all links on the page with class "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"
        for a_href in soup.find_all("a", {"class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"}):
            # Get the href attribute of each link and add it to the href_list
            href_list.append(a_href.get('href'))

        # Print the list of href links
        print(href_list)

        # Exit the loop
        break
