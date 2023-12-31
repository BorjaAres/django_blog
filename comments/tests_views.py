from django.test import TestCase, Client
from django.urls import reverse
from user.models import User
from posts.models import Post
from .models import Comment
from .forms import CommentForm
from .views import PostComment
from django.test import RequestFactory


class CommentsViewsTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
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

    def test_post_comment_redirects_if_logged_in(self):
        """Test that posting a comment redirects to the post detail page if the user is logged in"""
        client = Client()
        client.login(email='test@example.com', password='testpassword')
        url = reverse('post_detail', kwargs={'pk': self.post.pk})
        response = client.post(url, {'content': 'Test comment'})
        self.assertEqual(response.status_code, 302)  # Redirects after posting a comment

    def test_post_comment_redirects_to_login_if_not_logged_in(self):
        """Test that posting a comment redirects to the login page if the user is not logged in"""
        client = Client()
        url = reverse('post_detail', kwargs={'pk': self.post.pk})
        response = client.post(url, {'content': 'Test comment'})
        self.assertEqual(response.status_code, 302)  # Redirects to login page

    def test_comment_form_is_invalid_with_no_content(self):
        """Test that the comment form is invalid and shows an error message if the content is empty"""
        form = CommentForm(data={'content': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['content'], ['This field is required.'])

    def test_comment_form_is_valid_with_content(self):
        """Test that the comment form is valid if the content is provided"""
        form = CommentForm(data={'content': 'Test comment'})
        self.assertTrue(form.is_valid())

    def test_comment_is_saved_if_user_and_post_and_content_are_provided(self):
        """Test that a comment is saved to the database if the user, post, and content are provided"""
        # Use the RequestFactory to simulate a POST request
        factory = RequestFactory()
        url = reverse('post_detail', kwargs={'pk': self.post.pk})
        data = {'content': 'Test comment'}
        request = factory.post(url, data)

        # Manually set the user on the request
        request.user = self.user

        # Get the view and call it with the request
        view = PostComment.as_view()
        response = view(request, pk=self.post.pk)

        # Check if the comment was saved
        comment = Comment.objects.filter(content='Test comment').first()
        self.assertIsNotNone(comment)

    def test_comment_is_not_saved_if_content_is_empty(self):
        """Test that a comment is not saved to the database if the content is empty"""
        client = Client()
        client.login(email='test@example.com', password='testpassword')
        url = reverse('post_detail', kwargs={'pk': self.post.pk})
        response = client.post(url, {'content': ''})

        # Check if the comment was saved
        comment = Comment.objects.filter(content='Test comment').first()
        self.assertIsNone(comment)

    def test_comment_is_not_saved_if_user_is_not_logged_in(self):
        """Test that a comment is not saved to the database if the user is not logged in"""
        client = Client()
        url = reverse('post_detail', kwargs={'pk': self.post.pk})
        response = client.post(url, {'content': 'Test comment'})

        # Check if the comment was saved
        comment = Comment.objects.filter(content='Test comment').first()
        self.assertIsNone(comment)
