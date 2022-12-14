from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from feeds.models import Feed
from feeds import exceptions
import logging
logger = logging.getLogger(__name__)


class FollowFeed(APIView):
    """get feed_id and user(by header bearer) then add user to feed followers"""
    permission_classes = [permissions.IsAuthenticated,]
    def post(self, request):
        try:
            user = request.user
            feed_id = request.data['feed_id']
            if  Feed.objects.filter(pk=feed_id,followers=user).exists():
                feed = Feed.objects.get(pk=feed_id)
                feed.followers.remove(request.user)
                return Response({'message':"unfollowed  this feed succsessfuly !" },status=status.HTTP_200_OK)
            else:
                feed_id= request.data['feed_id']
                feed = Feed.objects.get(pk=feed_id)
                feed.followers.add(user)
                return Response({'message': 'you followed this feed succsessfuly '}, status=status.HTTP_200_OK)
        except Feed.DoesNotExist:
            raise exceptions.NotFound("feed not found")
        except KeyError as e:
            raise exceptions.MissingParameter(e)
        except Exception as e:
            logger.error(e)
            raise exceptions.InternalServerError()
