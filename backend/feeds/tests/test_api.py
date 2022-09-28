import datetime
from django.test import TestCase


from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from accounts.models import User
from feeds.models import Feed,Item
from accounts.models import User

class FeedsTest(TestCase):
    """ Test module for feeds api """

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
        self.feed.followers.add(self.user)
        self.item = Item.objects.create(
            title='test item',
            link='https://test.com',
            description='test description',
            pub_date=datetime.datetime.now(),
            feed=self.feed
        )

    def test_get_feeds(self):
        response = self.client.get(reverse('feedslist'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_items(self):
        response = self.client.get(reverse('itemslist'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_my_items(self):
        response = self.client.get(reverse('getmyitems'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_item_detail(self):
        response = self.client.get(reverse('itemdetail',args=[self.item.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'test item')
    
    def test_follow_feed(self):
        response = self.client.post(reverse('followfeed'),{'feed_id':self.feed.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'you followed this feed succsessfuly ')
        
    
    def test_unfollow_feed(self):
        response = self.client.post(reverse('unfollowfeed'),{'feed_id':self.feed.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'you unfollowed this feed succsessfuly ')


        