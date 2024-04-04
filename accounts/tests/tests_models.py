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

    def test_raise_error_message_when_no_email_set(self):
        with self.assertRaisesMessage(ValueError,'The Email Must be set'):
            User.objects.create_user(email='', password='password45')

    def test_raise_error_message_when_no_password_provided(self):
        with self.assertRaisesMessage(ValueError,'The password Must be provided'):
            User.objects.create_user(email='fada@gmail.com', password='')

    def test_raise_error_message_when_password_less_than_eight(self):
        with self.assertRaisesMessage(ValueError,'Password should be more than 8 Characters'):
            User.objects.create_user(email='fada@gmail.com', password='less')

    def test_create_superuser_without_is_staff(self):
        with self.assertRaisesMessage(ValueError,'Superuser must have is_staff=True'):
            User.objects.create_superuser(email='fada@gmail.com', password='password45', is_staff=False)

    def test_create_superuser_without_is_superuser(self):
        with self.assertRaisesMessage(ValueError,'Superuser must have is_superuser=True'):
            User.objects.create_superuser(email='fada@gmail.com', password='password45', is_superuser=False)
