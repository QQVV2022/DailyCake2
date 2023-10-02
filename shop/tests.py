from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Users, Product
from datetime import datetime


# Create a django model test class name Model_Test inheriting from the TestCase class
class Model_Test(TestCase):
    #create set up function to create  a user profile
    def setUp(self):
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
    # create set up function to create  a user
    def setUp(self):
        self.user = Users.objects.create_user(username='abc123', email="test@email.com", password='12345', is_active=True, create_time=datetime.now(), last_modify_time=datetime.now())
        self.user.save()
        self.client = Client()
        # create a Product object
        self.product = Product.objects.create(title='cupCake', price=100, discount_price=80.0, category='test_category', description='test_description')
        self.product.save()

    def tearDown(self):
        self.user.delete()
        self.product.delete()
        # self.client.logout()


    #create test function to test the if user exist
    def test_user_exist(self):
        # check if the user exist
        self.assertEqual(self.user.username, 'abc123')


    # create a function to visit index page
    def test_index_page(self):
        # response = self.client.get('/')
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/index.html')

    # create a test function to visit detail page
    def test_detail_page(self):
        url = reverse('detail', kwargs={'id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/detail.html')

    def test_user_login(self):
        response = self.client.post(reverse("signinlogin"), {'user_name': 'abc123', 'password': '12345'})
        print("**login**",response)
        # assert if response status code is 200
        self.assertEqual(response.status_code, 302)
        # assert if response will redirect to the index page
        self.assertRedirects(response, '/')

    # create a test function to register a user
    def test_user_register(self):
        response = self.client.post(reverse("signup"), {'user_name': 'ppp', 'email': 'XX@XX.com', 'password': '12345', 'repeat_password':'12345', 'allow': 'on'})
        # assert if response will redirect to the index page
        self.assertRedirects(response, '/')

    # create a test function to test the user logout
    def test_user_logout(self):
        response = self.client.get(reverse("signout"))
        # assert if response will redirect to the index page
        self.assertRedirects(response, '/')

    # create a test function to place order
    def test_place_order(self):
        prods = [{"id":1,"name":"cupCake","price":100,"count":2}]
        response = self.client.post(reverse("placeorder"), {'products': prods, 'firstname': 'XXXXXXXX', 'lastname': 'XXXXXXXX','price':200, 'address': 'XXXXXXXX','email': 'XXXXXXXX', 'phone': 'XXXXXXXX'})
        # assert status code is 302
        self.assertEqual(response.status_code, 302)
        # assert if response will redirect to the index page
        self.assertRedirects(response, '/')

    # create a test function to change passwor
    def test_change_password(self):
        old_password = '12345'
        # u = User.objects.get(username='abc123')
        # print("######",u.check_password('12345'))
        response = self.client.post(reverse("changepassword"), {'user_name': 'abc123','email':'test@email.com', 'password': '123456', 'repeat_password': '123456'})
        u = User.objects.get(username='abc123')
        self.assertEqual(u.check_password('123456'), True)









