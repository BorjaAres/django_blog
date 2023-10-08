from django.test import TestCase, Client
from django.urls import reverse

class TestUtilitiesViews(TestCase):
    """Test case for the views in the Utilities app."""

    def test_index_page(self):
        """Test that the index page loads correctly."""
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_contact_page(self):
        """Test that the contact page loads correctly."""
        client = Client()
        response = client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_about_us_page(self):
        """Test that the about us page loads correctly."""
        client = Client()
        response = client.get(reverse('about_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about_us.html')
