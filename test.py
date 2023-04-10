import requests
from bs4 import BeautifulSoup

base_url = 'https://www.amazon.in/s?k=monitors'
page_num = 1
has_next_page = True

while has_next_page:
    url = base_url + '&page=' + str(page_num)
    response = requests.get(url)
    
    if response.status_code == 200:
        print('Scraping page', page_num)
    else:
        print('Request failed for page', page_num)
        continue
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    monitor_names = soup.find_all('span', {'class': 'a-size-medium a-color-base a-text-normal'})
    monitor_prices = soup.find_all('span', {'class': 'a-price-whole'})
    product_links = soup.find_all('a', {'class': 'a-link-normal a-text-normal'})
    review_ratings = soup.find_all('span', {'class': 'a-icon-alt'})
    
    for name, price, link, rating in zip(monitor_names, monitor_prices, product_links, review_ratings):
        print(name.text.strip())
        print('Price:', price.text.strip())
        print('Link:', 'https://www.amazon.in' + link['href'])
        print('Rating:', rating.text.strip())
        print('---')
        
    next_button = soup.find('span', {'class': 's-pagination-item s-pagination-next s-pagination-disabled'})
    has_next_page = False if next_button else True
    page_num += 1
