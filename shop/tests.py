from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Users
from datetime import datetime
from django.db import models


# Create a django model test class name Model_Test inheriting from the TestCase class
class Model_Test(TestCase):
    #create set up function to create a user and a user profile
    def setUp(self):
        # self.user = User.objects.create_user(username='XXXXXXXX', password='12345')
        # self.user.save()
        # self.user_profile = Users.objects.create(user=self.user, phone_number='07777777777', address='test address')
        self.user_profile = Users.objects.create_user(username='XXXXXXXX', email="test@email.com", password='12345', is_active=True, create_time=datetime.now(), last_modify_time=datetime.now())

        self.user_profile.save()

        self.client = Client()

    #create tear down function to delete the user and the user profile
    def tearDown(self):
        # self.user.delete()
        self.user_profile.delete()

    #create test function to test the user and the user profile
    def test_user_profile(self):
        #check if the user is created
        self.assertEqual(self.user_profile.username, 'XXXXXXXX')
        #check if the user profile is created
        self.assertEqual(self.user_profile.email, 'test@email.com')  ## register a user successfully


# create a test function to test the user login
class User_Login_Test(TestCase):
    def setUp(self):
        self.user = Users.objects.create_user(username='XXXXXXXX', email="test@email.com", password='12345', is_active=True, create_time=datetime.now(), last_modify_time=datetime.now())

        self.user.save()

        self.client = Client()

    def tearDown(self):
        self.user.delete()

    def test_user_login(self):
        response = self.client.post('/login/', {'username': 'XXXXXXXX', 'password': '12345'})
        print("****",response)
        self.assertTemplateUsed(response, 'shop/signin.html')
        # assert html





