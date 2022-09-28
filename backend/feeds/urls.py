from django.urls import path
from feeds.views.feeds import FeedsList,ItemsList,GetMyItems,ItemDetailView
from feeds.views.users import FollowFeed,UnFollowFeed

urlpatterns = [
    path('feeds/', FeedsList.as_view(), name='feedslist'),
    path('items/', ItemsList.as_view(), name='itemslist'),
    path('myitems/', GetMyItems.as_view(), name='getmyitems'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='itemdetail'),
    path('follow-feed/', FollowFeed.as_view(), name='followfeed'),
    path('unfollow-feed/', UnFollowFeed.as_view(), name='unfollowfeed'),
]
