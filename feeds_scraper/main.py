# feeds scraper

import requests
from bs4 import BeautifulSoup

def rss_scraper(url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, features='xml')

        feed = {
            'title': soup.find('title').text,
            'link': soup.find('link').text,
            'description': soup.find('description').text,
            'pubDate': soup.find('pubDate').text,
            'items': []
        }

        items = soup.findAll('item')
        for item in items:
            feed['items'].append({
                'title': item.find('title').text,
                'link': item.find('link').text,
                'description': item.find('description').text,
                'pubDate': item.find('pubDate').text,
            })

        return feed





feed=rss_scraper("https://news.ycombinator.com/rss")
print(feed)