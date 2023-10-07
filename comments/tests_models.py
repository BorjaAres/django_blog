from django.test import TestCase
from posts.models import Post
from.models import Comment
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

User = get_user_model()

class BlogModelTests(TestCase):
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
            image='posts_images/test_image.jpg',
            author=self.user
        )

    def test_comment_creation(self):
        # Create a test Comment instance
        comment = Comment.objects.create(
            post=self.post,
            user=self.user,
            content='This is a test comment.'
        )

        # Check if the Comment instance was created successfully
        self.assertEqual(comment.post.title, 'Test Post')
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.content, 'This is a test comment.')

    def test_comment_creation_without_user(self):
        # Attempt to create a test Comment instance without a user
        with self.assertRaises(IntegrityError):
            comment = Comment.objects.create(
                post=Post.objects.create(
                    title='Test Post',
                    content='This is a test post content.',
                    author=self.user
                ),
                content='This is a test comment.'
            )

    def test_comment_creation_without_post(self):
        # Attempt to create a test Comment instance without a post
        with self.assertRaises(IntegrityError):
            comment = Comment.objects.create(
                user=self.user,
                content='This is a test comment.'
            )

    def test_comment_creation_without_content(self):
        # Attempt to create a test Comment instance without content
        with self.assertRaises(IntegrityError):
            comment = Comment.objects.create(
                post=self.post,
                user=self.user,
                content=None
            )


