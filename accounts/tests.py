from django.contrib.auth.models import User
from django.test import TestCase, SimpleTestCase
from django.urls import resolve, reverse
from .views import RegisterUserView, index


class TestUrlsAcc(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func.view_class, RegisterUserView)

    def test_list_url_is_resolved(self):
        url = reverse('restindex')
        self.assertEqual(resolve(url).func, index)
