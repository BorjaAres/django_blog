from django.test import TestCase, Client
from django.urls import reverse
from user.models import User
from posts.models import Post
from .models import Comment
from .forms import CommentForm
from django_webtest import WebTest

class BlogViewsTests(TestCase, WebTest):
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

    def test_post_comment_view(self):
        client = Client()
        client.login(username='testuser', password='testpassword')
        url = reverse('post_detail', kwargs={'pk': self.post.pk})
        response = client.post(url, {'content': 'Test comment'})
        self.assertEqual(response.status_code, 302)  # Redirects after posting a comment

    def test_post_comment_view_without_login(self):
        client = Client()
        url = reverse('post_detail', kwargs={'pk': self.post.pk})
        response = client.post(url, {'content': 'Test comment'})
        self.assertEqual(response.status_code, 302)  # Redirects to login page

    def test_post_comment_view_with_no_content(self):
        # Test with empty content
        form = CommentForm(data={'content': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['content'], ['This field is required.'])

        # Test with non-empty content
        form = CommentForm(data={'content': 'Test comment'})
        self.assertTrue(form.is_valid())

    # def test_comment_is_saved(self):
    #     # Use the WebTest user method to log in
    #     self.app.set_user(self.testuser)
    #
    #     # Get the URL for the post detail view
    #     url = reverse('post_detail', kwargs={'pk': self.testpost.pk})
    #
    #     # Use the WebTest app to post a comment
    #     response = self.app.post(url, params={'content': 'Test comment'}, status=302)
    #
    #     # Check if the comment was saved
    #     comment = Comment.objects.filter(content='Test comment').first()
    #     self.assertIsNotNone(comment)

    def test_comment_is_not_saved_if_content_is_empty(self):
        client = Client()
        client.login(username='testuser', password='testpassword')
        url = reverse('post_detail', kwargs={'pk': self.post.pk})
        response = client.post(url, {'content': ''})

        # Check if the comment was saved
        comment = Comment.objects.filter(content='Test comment').first()
        self.assertIsNone(comment)

    def test_comment_is_not_saved_if_user_is_not_logged_in(self):
        client = Client()
        url = reverse('post_detail', kwargs={'pk': self.post.pk})
        response = client.post(url, {'content': 'Test comment'})

        # Check if the comment was saved
        comment = Comment.objects.filter(content='Test comment').first()
        self.assertIsNone(comment)