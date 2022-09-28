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


class GetMyItems(ListAPIView):
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Item.objects.filter(feed__followers=user).select_related('feed').all()
#retrieve the feed by pk 
class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.prefetch_related('read').select_related('feed').all()
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
            if not Item.objects.filter(pk=item.pk,read=user).exists():
                item.read.add(user)
            return super().get(request, *args, **kwargs)
        except Item.DoesNotExist:
            return Response({'message':"item not found !" },status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            msg = f"Error: {e}"
            return Response(msg, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

