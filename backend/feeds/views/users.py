import re
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView,ListAPIView,RetrieveAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from feeds.serializers import FeedSerializer,ItemSerializer
from feeds.models import Feed,Item
from accounts.models import User



class FollowFeed(APIView):
    """get feed_id and user(by header bearer) then add user to feed followers"""
    permission_classes = [permissions.IsAuthenticated,]
    def post(self, request):
        try:
            feed_id= request.data['feed_id']
            feed = Feed.objects.get(pk=feed_id)
            user = request.user
            feed.followers.add(user)
            return Response({'message': 'you followed this feed succsessfuly '}, status=status.HTTP_200_OK)
        except Feed.DoesNotExist:
            return Response({'message':"feed not found !" },status=status.HTTP_404_NOT_FOUND)
        except KeyError as e:
            msg = f"Missing key: {e}"
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            msg = f"Error: {e}"
            return Response(msg, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UnFollowFeed(APIView):
    """get feed_id and user(by header bearer) then remove user from feed followers"""
    permission_classes = [permissions.IsAuthenticated,]
    def post(self, request):
        try:
            feed_id= request.data['feed_id']
            feed = Feed.objects.get(pk=feed_id)
            user = request.user
            # if user is not in followers list return error
            if not Feed.objects.filter(pk=feed_id,followers=user).exists():
                return Response({'message':"you are not following this feed !" },status=status.HTTP_400_BAD_REQUEST)
            feed.followers.remove(user)
            return Response({'message': 'you unfollowed this feed succsessfuly '}, status=status.HTTP_200_OK)
        except Feed.DoesNotExist:
            return Response({'message':"feed not found !" },status=status.HTTP_404_NOT_FOUND)
        except KeyError as e:
            msg = f"Missing key: {e}"
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            msg = f"Error: {e}"
            return Response(msg, status=status.HTTP_500_INTERNAL_SERVER_ERROR)