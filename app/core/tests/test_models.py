from django.test import TestCase
from django.contrib.auth import get_uer_model

class ModelTests(TestCase):
    def test_create_user_with_email_succesful(self):
        email = "test@example.com"
        password = 'test123'
        user = get_uer_model().objects.create_user(
            email = email,
            password = password,
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
