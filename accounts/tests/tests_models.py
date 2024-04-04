from rest_framework.test import APITestCase
from accounts.models import User


class TestModel(APITestCase):

    def test_creates_user(self):
        user=User.objects.create_user('dafa@gmail.com','dafadafa89')
        self.assertIsInstance(user,User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email,'dafa@gmail.com')

    def test_str_method_with_email(self):
        user = User(email='dafa@gmail.com') # create an email instance
        outcome = user.__str__()
        self.assertEqual(outcome,'dafa@gmail.com') #checks if the return value matches the expected

    def test_str_method_without_email(self):
        user = User()
        outcome = user.__str__()
        self.assertEqual(outcome, '') #checks if the returned value is an empty string

    def test_token_property(self):
        user = User()
        result = user.token
        self.assertEqual(result,'')

    def test_create_superuser(self):
        user = User.objects
        superuser = user.create_superuser(email='fada@gmail.com',password='password80')
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)