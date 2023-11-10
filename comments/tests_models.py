from django.test import TestCase
from posts.models import Post
from .models import Comment
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

User = get_user_model()


class CommentModelTests(TestCase):
    def setUp(self):
        """
        Set up a test user and a test post instance for use in the tests.
        """
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            image='posts_images/test_image.jpg',
            author=self.user
        )

    def test_successful_comment_creation(self):
        """
        Test that a comment can be successfully created with valid data.
        """
        comment = Comment.objects.create(
            post=self.post,
            user=self.user,
            content='This is a test comment.'
        )

        self.assertEqual(comment.post.title, 'Test Post')
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.content, 'This is a test comment.')

    def test_comment_creation_without_user_fails(self):
        """
        Test that attempting to create a comment without a user raises an IntegrityError.
        """
        with self.assertRaises(IntegrityError):
            comment = Comment.objects.create(
                post=Post.objects.create(
                    title='Test Post',
                    content='This is a test post content.',
                    author=self.user
                ),
                content='This is a test comment.'
            )

    def test_comment_creation_without_post_fails(self):
        """
        Test that attempting to create a comment without a post raises an IntegrityError.
        """
        with self.assertRaises(IntegrityError):
            comment = Comment.objects.create(
                user=self.user,
                content='This is a test comment.'
            )

    def test_comment_creation_without_content_fails(self):
        """
        Test that attempting to create a comment without content raises an IntegrityError.
        """
        with self.assertRaises(IntegrityError):
            comment = Comment.objects.create(
                post=self.post,
                user=self.user,
                content=None
            )

    def test_str_representation(self):
        """
        Test that the string representation of a comment is correct.
        """
        comment = Comment.objects.create(
            post=self.post,
            user=self.user,
            content='This is a test comment.'
        )

        self.assertEqual(str(comment), 'This is a test comment. | test@example.com | Test Post')
