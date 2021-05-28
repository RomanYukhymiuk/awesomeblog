from django.contrib.auth.models import User
from django.test import TestCase, SimpleTestCase
from django.urls import resolve, reverse
from .views import HomeView, PostDetailView, CreatePostView

from .models import Post

class PostTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="Admin")
        Post.objects.create(author=self.user1,
                            title="Test post",
                            body="Testing body post",)

    def test_post_is_posted(self):
        """Posts are created"""
        post1 = Post.objects.get(title="Test post")
        self.assertEqual(post1.body, "Testing body post")

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, HomeView)

    def test_list_url_is_resolved(self):
        url = reverse('post-detail')
        self.assertEqual(resolve(url).func.view_class, PostDetailView)

    def test_list_url_is_resolved(self):
        url = reverse('post-new')
        self.assertEqual(resolve(url).func.view_class, CreatePostView)
