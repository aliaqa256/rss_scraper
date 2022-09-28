from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView,ListAPIView,RetrieveAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from feeds.serializers import FeedSerializer,ItemSerializer
from feeds.models import Feed,Item


class FeedsList(ListAPIView):
    queryset = Feed.objects.prefetch_related('followers').all()
    serializer_class = FeedSerializer
    permission_classes = [permissions.IsAuthenticated]


class ItemsList(ListAPIView):
    queryset = Item.objects.prefetch_related('read').select_related('feed').all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

