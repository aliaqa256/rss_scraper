
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView,ListAPIView,RetrieveAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from .throttles import LoginPerDayThrottle
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserRegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User



class LoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
    # throttle_classes = [LoginPerDayThrottle]
    queryset = User.objects.all()

class RegistrationView(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegisterSerializer

    def create(self, request):
        data = UserRegisterSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)