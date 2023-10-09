from django.test import TestCase, SimpleTestCase, override_settings
from django.urls import reverse, resolve
from .models import User, Post
from .views import BlogHomeView, PostDetailView, AllPostsView, PostCreateView


@override_settings(ROOT_URLCONF='posts.urls')
class StatusCodeTests(TestCase):
    """
    Test case for checking the status codes of the views in the posts app.
    """

    def test_blog_home_status_code(self):
        """
        Test that the blog home view returns a status code of 200 (OK).
        """
        url = reverse('blog_home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_detail_status_code(self):
         """
         Test that the post detail view returns a status code of 200 (OK) with a valid post id.
         """
         url = reverse('post_detail', args=[self.post.id])
         response = self.client.get(url)
         self.assertEqual(response.status_code, 200)

    def test_all_posts_status_code(self):
         """
         Test that the all posts view returns a status code of 200 (OK).
         """
         url = reverse('all_posts')
         response = self.client.get(url)
         self.assertEqual(response.status_code, 200)

    def test_post_create_status_code(self):
         """
         Test that the post create view returns a status code of 200 (OK).
         """
         url = reverse('post_create')
         response = self.client.get(url)
         self.assertEqual(response.status_code, 200)

@override_settings(ROOT_URLCONF='posts.urls')
class ViewResolutionTests(SimpleTestCase):
    """
    Test case for checking that URLs resolve to the correct views in the posts app.
    """

    def test_blog_home_resolves(self):
        """
        Test that the URL for the blog home view resolves to the correct view.
        """
        url = reverse('blog_home')
        self.assertEqual(resolve(url).func.view_class, BlogHomeView)

    def test_post_detail_resolves(self):
        """
        Test that the URL for the post detail view resolves to the correct view.
        """
        url = reverse('post_detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, PostDetailView)

    def test_all_posts_resolves(self):
        """
        Test that the URL for the all posts view resolves to the correct view.
        """
        url = reverse('all_posts')
        self.assertEqual(resolve(url).func.view_class, AllPostsView)

    def test_post_create_resolves(self):
        """
        Test that the URL for the post create view resolves to the correct view.
        """
        url = reverse('post_create')
        self.assertEqual(resolve(url).func.view_class, PostCreateView)

@override_settings(ROOT_URLCONF='posts.urls')
class URLPatternTests(TestCase):
    """
    Test case for checking that URL patterns are correct in the posts app.
    """

    def test_blog_home_pattern(self):
        """
        Test that the blog home URL pattern is correct.
        """
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)

    def test_all_posts_pattern(self):
        """
        Test that the all posts URL pattern is correct.
        """
        response = self.client.get('/posts/all_posts/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url_pattern(self):
        user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword',
        )

        post = Post.objects.create(
            title='Test Post',
            content='Test content',
            author=user,
        )

        response = self.client.get(f'/posts/{post.id}/')
        self.assertEqual(response.status_code, 200)


    def test_post_create_pattern(self):
        """
        Test that the post create URL pattern is correct.
        """
        response = self.client.get('/posts/post/new/')
        self.assertEqual(response.status_code, 403)

