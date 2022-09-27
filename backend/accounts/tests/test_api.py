from django.test import TestCase

#  regiser and login test case  with simple jwt
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from accounts.models import User
from django.conf import settings


class UserRegistrationTestCase(TestCase):
    """ Test module for user registration """

    def setUp(self):
        self.client = APIClient()

    def test_registration(self):
        """ Test registration with valid payload """
        payload = {
            'username': 'testuser',
            'email': 'alilotfi256@gmail.com',
            'password': '@Testpass',
            'confirm_password': '@Testpass',
            'full_name': 'testuser',
        }
        response = self.client.post(
            reverse('Registration_View'),
            payload
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(username=payload['username'])
        self.assertEqual(user.username, payload['username'])



    def test_registration_invalid_payload(self):
        """ Test registration with invalid payload """
        payload = {
            'username': 'testuser',
            'email': 'alilotfi256@gmail.com',
            'password': 'testpass',
            'password2': 'testpass'
        }
        response = self.client.post(
            reverse('Registration_View'),
            payload
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



class LoginViewTestCase(TestCase):
    """ Test module for user login """

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(
            username='testuser',
            password='testpassword',
            email='alilotfi256@gmail.com')


    def test_login_valid_credentials(self):
        """ Test login with valid payload """
        payload = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(
            reverse('login_view'),
            payload
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
