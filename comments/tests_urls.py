from django.urls import reverse
from django.test import TestCase

class MyTests(TestCase):
    def test_example_url(self):
        url = reverse('example')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
