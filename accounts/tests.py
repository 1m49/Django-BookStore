from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class SignUpTests(TestCase):
    username = 'iman akbari'
    email = 'iman.ach007@gmail.com'

    def test_signup_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_form(self):
        user = get_user_model().objects.create_user(
            self.username,
            self.email,
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, 'iman akbari')
        self.assertEqual(get_user_model().objects.all()[0].email, 'iman.ach007@gmail.com')
