import requests
from bs4 import BeautifulSoup
def scraper(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features='xml')
    items_list = []
    items = soup.findAll('item')
    for item in items:
        items_list.append({
            'title': item.find('title').text,
            'link': item.find('link').text,
            'description': item.find('description').text,
            'pub_date': item.find('pubDate').text,
        })
    return items_list