from django.test import TestCase, Client
from django.urls import reverse
from user.models import User
from .models import Post
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied


class TestPostsViews(TestCase):
    """Test case for the views in the Posts app."""

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
            author=self.user
        )

    def test_blog_home_page(self):
        """Test that the blog home page loads correctly."""
        client = Client()
        response = client.get(reverse('blog_home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_home.html')

    def test_all_posts_page(self):
        """Test that the all posts page loads correctly."""
        client = Client()
        response = client.get(reverse('all_posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'all_posts.html')

    def test_post_detail_page(self):
        """Test that an individual post's detail page loads correctly."""
        client = Client()
        url = reverse('post_detail', kwargs={'pk': self.post.pk})
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_form_page(self):
        """Test that the post form page loads correctly."""
        self.user = User.objects.create_superuser(
            username='testadmin',
            email='testadmin@example.com',
            password='testpassword'
        )

        client = Client()
        # Log in as the superuser
        client.login(email='testadmin@example.com', password='testpassword')

        response = client.get(reverse('post_create'))
        self.assertTemplateUsed(response, 'post_form.html')

    def test_create_post_form_page_is_forbidden(self):
        """Test that the post is forbidden if not superuser."""
        client = Client()
        response = client.get(reverse('post_create'))
        self.assertEqual(response.status_code, 403)

    def test_create_post_as_superuser_is_valid(self):
        """Test that a superuser can access the post creation page."""
        # Create a test superuser
        self.user = User.objects.create_superuser(
            username='testsuperuser',
            email='testsuper@example.com',
            password='testpassword'
        )

        client = Client()
        client.login(email='testsuper@example.com', password='testpassword')

        response = client.get(reverse('post_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_form.html')

    def test_create_post_as_staff_is_valid(self):
        """Test that a staff member can access the post creation page."""
        # Create a test staff member
        self.user = User.objects.create_user(
            is_staff=True,
            username='teststaff',
            email='staff@example.com',
            password='testpassword'
        )

        client = Client()
        client.login(email='staff@example.com', password='testpassword')

        response = client.get(reverse('post_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_form.html')

    def test_create_post_page_as_normal_user_is_forbidden(self):
        """Test that a normal user cannot access the post creation page."""

        client = Client()
        client.login(username='testuser', password='testpassword')

        response = client.get(reverse('post_create'))

        self.assertEqual(response.status_code, 403)

    def test_search_results_with_valid_query(self):
        # Send a GET request with a valid search query
        response = self.client.get(reverse('search_results'), {'q': 'Test'})

        # Check if the response status code is 200 (success)
        self.assertEqual(response.status_code, 200)

        # Check if the posts containing the search query are in the context
        self.assertIn(self.post, response.context['posts'])
        self.assertIn(self.post, response.context['posts'])

        # Check if the posts not containing the search query are not in the context
        self.assertNotIn('Nonexistent Post', response.context['posts'])

        # Check if the correct template is used
        self.assertTemplateUsed(response, 'search_results.html')

    def test_search_results_with_empty_query(self):
        # Send a GET request with an empty search query
        response = self.client.get(reverse('search_results'), {'q': ''})

        # Check if the response status code is 200 (success)
        self.assertEqual(response.status_code, 200)

        # Check if the context contains the appropriate message for no results
        self.assertContains(response, 'No articles found.')

        # Check if the correct template is used
        self.assertTemplateUsed(response, 'search_results.html')

    def test_search_results_with_invalid_query(self):
        # Send a GET request with an invalid search query
        response = self.client.get(reverse('search_results'), {'q': 'InvalidQuery'})

        # Check if the response status code is 200 (success)
        self.assertEqual(response.status_code, 200)

        # Check if the context contains the appropriate message for no results
        self.assertContains(response, 'No articles found.')

        # Check if the correct template is used
        self.assertTemplateUsed(response, 'search_results.html')
