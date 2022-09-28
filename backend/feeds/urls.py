from django.urls import path
from . import views

urlpatterns = [
    path('feeds/', views.FeedsList.as_view(), name='feedslist'),
    path('items/', views.ItemsList.as_view(), name='itemslist'),
]
