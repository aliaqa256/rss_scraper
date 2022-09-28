from django.urls import path
from feeds.views.feeds import FeedsList,ItemsList
from feeds.views.users import FollowFeed,UnFollowFeed

urlpatterns = [
    path('feeds/', FeedsList.as_view(), name='feedslist'),
    path('items/', ItemsList.as_view(), name='itemslist'),
    path('follow-feed/', FollowFeed.as_view(), name='followfeed'),
    path('unfollow-feed/', UnFollowFeed.as_view(), name='unfollowfeed'),
]
