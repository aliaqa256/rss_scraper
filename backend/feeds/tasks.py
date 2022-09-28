from .utils import scraper
from celery import shared_task
from datetime import datetime

from .models import Feed

@shared_task
def rss_scraper():
    feeds=Feed.objects.all()
    for feed in feeds:
        feed_items=scraper(feed.url)
        for item in feed_items:
            if not feed.items.filter(link=item['link']).exists():
                item['pub_date']=datetime.strptime(item['pub_date'], '%a, %d %b %Y %H:%M:%S %z')
                feed.items.create(**item)