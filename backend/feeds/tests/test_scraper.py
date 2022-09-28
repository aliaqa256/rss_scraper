import datetime
from re import S, T
import time
from django.test import TestCase, override_settings


from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from accounts.models import User
from feeds.models import Feed,Item
from accounts.models import User
from feeds.tasks import rss_scraper


class ScraperTest(TestCase):
    """ Test module for Scraper task"""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(
            username='testuser',
            password='testpassword',
            email='alilotfi256@gmail.com')
        self.client.force_authenticate(user=self.user)
        # create dummy data
        self.feed = Feed.objects.create(
            title='hacker news',
            url='https://news.ycombinator.com/rss',
        )
    def test_scraper(self):
        #get resualt of celery task
        resualt=rss_scraper.apply().get()
        print(resualt)
        self.assertEqual(resualt, 'done')
    
    def test_scraper_with_wrong_url(self):
        self.feed.url='https://news.ycombinator.com/rss1'
        self.feed.save()
        resualt=rss_scraper.apply().get()
        self.assertEqual(resualt, 'error')

