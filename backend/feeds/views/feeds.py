from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from feeds.serializers import FeedSerializer,ItemSerializer
from feeds.models import Feed,Item
from accounts.models import User
from django.shortcuts import get_object_or_404
from feeds import exceptions
import logging
logger = logging.getLogger(__name__)


class FeedsList(ListAPIView):
    queryset = Feed.objects.prefetch_related('followers').all()
    serializer_class = FeedSerializer
    permission_classes = [permissions.IsAuthenticated]


class ItemsList(ListAPIView):
    queryset = Item.objects.prefetch_related('read_by').select_related('feed').all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class GetMyFeeds(ListAPIView):
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Item.objects.prefetch_related('read_by').select_related('feed').all()
    def get(self, request, pk):
        user=get_object_or_404(User, pk=pk)
        if pk is not request.user.id:
            raise exceptions.AccessDenied("this content is not yours")
        items = self.get_queryset().filter(feed__followers=pk)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.prefetch_related('read_by').select_related('feed').all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated,]
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        try:
            # check of the user is following the feed
            if not Item.objects.filter(pk=kwargs['pk'],feed__followers=request.user).exists():
                return Response({'message':"you are not following this feed !" },status=status.HTTP_400_BAD_REQUEST)
            item = self.get_object()
            user = request.user
            if not Item.objects.filter(pk=item.pk,read_by=user).exists():
                item.read_by.add(user)
            return super().get(request, *args, **kwargs)
        except Item.DoesNotExist:
            raise exceptions.NotFound("item not found")
        except Exception as e:
            logger.error(e)            
            raise exceptions.InternalServerError()

