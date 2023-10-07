from django.test import TestCase, Client
from django.urls import reverse
from user.models import User
from .models import Post
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied


class PostsViewsTests(TestCase):
    def setUp(self):
        def setUp(self):
            # Create a test superuser
            self.user = User.objects.create_superuser(
                username='testuser',
                email='test@example.com',
                password='testpassword'
            )

            # Create a test Post instance
            self.post = Post.objects.create(
                title='Test Post',
                content='This is a test post content.',
                author=self.user
            )

    def test_blog_home_view(self):
        client = Client()
        response = client.get(reverse('blog_home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_home.html')

    def test_all_posts_view(self):
        client = Client()
        response = client.get(reverse('all_posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'all_posts.html')

    def test_post_detail_view(self):
        client = Client()
        url = reverse('post_detail', kwargs={'pk': self.post.pk})
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_create_view(self):
        client = Client()
        client.login(username='testuser', password='testpassword')
        response = client.get(reverse('post_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_form.html')

