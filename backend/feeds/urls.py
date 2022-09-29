from django.urls import path
from feeds.views.feeds import FeedsList,ItemsList,GetMyFeeds,ItemDetailView
from feeds.views.users import FollowFeed

urlpatterns = [
    path('', FeedsList.as_view(), name='feedslist'),
    path('feeds/', ItemsList.as_view(), name='itemslist'),
    path('feeds/user/<int:pk>/', GetMyFeeds.as_view(), name='getmyitems'),
    path('feeds/<int:pk>/', ItemDetailView.as_view(), name='itemdetail'),
    path('feeds/follow/', FollowFeed.as_view(), name='followfeed'),
]
