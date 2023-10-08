from django.test import TestCase
from posts.models import Post
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.core.files.uploadedfile import SimpleUploadedFile

User = get_user_model()


class TestPostModel(TestCase):
    """Test case for the Post model in the Posts app."""

    def setUp(self):
        """Set up the test environment before each test method is run."""
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

    def test_post_creation_with_valid_data(self):
        """Test creating a post with valid data."""
        # Check if the Post instance was created successfully
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.content, 'This is a test post content.')
        self.assertEqual(self.post.image, 'posts_images/test_image.jpg')
        self.assertEqual(self.post.author, self.user)

    def test_post_creation_without_author_raises_integrity_error(self):
        """Test creating a post without an author raises an IntegrityError."""
        # Attempt to create a test Post instance without an author
        with self.assertRaises(IntegrityError):
            post = Post.objects.create(
                title='Test Post',
                content='This is a test post content.',
            )

    def test_post_creation_without_title_raises_integrity_error(self):
        """Test creating a post without a title raises an IntegrityError."""
        # Attempt to create a test Post instance without a title
        with self.assertRaises(IntegrityError):
            post = Post.objects.create(
                title=None,
                content='This is a test post content.',
                author=self.user
            )

    def test_post_creation_with_title_exceeding_max_length_raises_validation_error(self):
        """Test creating a post with a title longer than the maximum length raises a ValidationError."""
        # Attempt to create a Post instance with a title longer than the maximum length
        with self.assertRaises(ValidationError):
            post = Post(title='A' * 201, content='Some content', date='2023-01-01 12:00:00', author=self.user)
            post.full_clean()  # This will trigger the validation

    def test_post_creation_without_content_raises_integrity_error(self):
        """Test creating a post without content raises an IntegrityError."""
        # Attempt to create a test Post instance without content
        with self.assertRaises(IntegrityError):
            post = Post.objects.create(
                title='Test Post',
                content=None,
                author=self.user
            )

    def test_post_creation_without_image_is_valid(self):
        """Test creating a post without an image is valid."""
        # Create a test Post instance without an image
        post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            author=self.user
        )

        # Check if the Post instance was created successfully
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.content, 'This is a test post content.')
        self.assertEqual(post.image, '')
        self.assertEqual(post.author, self.user)

    def test_post_creation_with_invalid_image_type_raises_validation_error(self):
        """Test creating a post with an invalid image type raises a ValidationError."""

        # Create a temporary image file with an incorrect extension
        invalid_image_content = b'This is not an image content'
        invalid_image = SimpleUploadedFile("invalid_image.txt", invalid_image_content)

        # Attempt to create a Post instance with an invalid image type
        with self.assertRaises(ValidationError):
            post = Post(
                title='Test Post',
                content='This is a test post content.',
                image=invalid_image,
                author=self.user
            )
            post.full_clean()  # This will run all validators and raise ValidationError if any validator fails
