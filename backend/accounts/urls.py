from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login_view'),
    path('register-user/', views.RegistrationView.as_view(), name='Registration_View'),
]
