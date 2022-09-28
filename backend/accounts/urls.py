from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login_view'),
    path('refresh/', TokenRefreshView.as_view(), name='new_refresh_token'),
    path('register-user/', views.RegistrationView.as_view(), name='Registration_View'),
]
