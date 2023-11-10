from django.http import HttpResponse
from django.test import TestCase, Client
from django.core.mail import send_mail
from django.core import mail
from django.urls import reverse
from user.models import User


class TestUtilitiesViews(TestCase):
    """Test case for the views in the Utilities app."""

    def test_index_page(self):
        """Test that the index page loads correctly."""
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_about_us_page(self):
        """Test that the about us page loads correctly."""
        client = Client()
        response = client.get(reverse('about_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about_us.html')


class ContactViewTest(TestCase):

    def test_contact_page(self):
        """Test that the contact page loads correctly."""
        client = Client()
        response = client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_send_email(self):
        subject = 'Test Email'
        message = 'This is a test email sent using Mailtrap.'
        from_email = 'your_email@example.com'
        recipient_list = ['recipient@example.com']

        send_mail(subject, message, from_email, recipient_list)
        return HttpResponse('Test email sent!')

    def test_contact_form_submission_authenticated(self):
        # Create a user and log them in
        user = User.objects.create_user(username='testuser', password='testpassword', email='test@example.com')
        self.client.login(username='testuser', password='testpassword')

        post_data = {
            'message': 'Hello, this is a test message.',
        }

        response = self.client.post(reverse('contact'), post_data)

        # Check if the response status code is 200 (success)
        self.assertEqual(response.status_code, 200)

        # Check if an email was sent
        self.assertEqual(len(mail.outbox), 1)

        # Additional assertions specific to authenticated users

    def test_contact_form_submission_unauthenticated(self):
        # Log out the user (if needed)
        self.client.logout()

        post_data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'message': 'Hello, this is a test message.',
        }

        response = self.client.post(reverse('contact'), post_data)

        # Check if the response status code is 200 (success)
        self.assertEqual(response.status_code, 200)

        # Check if an email was sent
        self.assertEqual(len(mail.outbox), 1)
