from django.test import TestCase, SimpleTestCase, override_settings
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from user.views import UserLoginView, UserLogoutView, UserRegistrationView
from posts.views import PostCreateView, BlogHomeView, AllPostsView, PostDetailView
from utilities.views import IndexView, ContactView, AboutUsView
from posts.models import Post

User = get_user_model()


@override_settings(ROOT_URLCONF='utilities.urls')
class ViewResolutionTests(SimpleTestCase):
    """
    Test case for checking view resolution.
    """

    def test_index_view_resolution(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func.view_class, IndexView)

    def test_contact_view_resolution(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func.view_class, ContactView)

    def test_about_us_view_resolution(self):
        url = reverse('about_us')
        self.assertEqual(resolve(url).func.view_class, AboutUsView)



