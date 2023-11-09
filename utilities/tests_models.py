from django.test import TestCase
from .models import ContactMessage


class TestContactMessageModel(TestCase):
    def setUp(self):
        # Create a ContactMessage object for testing
        self.contact_message = ContactMessage.objects.create(
            name="John Doe",
            email="john@example.com",
            message="Hello, this is a test message."
        )

    def test_contact_message_str(self):
        # Test the __str__ method
        self.assertEqual(str(self.contact_message), "John Doe")

    def test_contact_message_count(self):
        # Test the count of ContactMessage objects
        contact_message_count = ContactMessage.objects.count()
        self.assertEqual(contact_message_count, 1)

    def test_contact_message_name(self):
        # Test the name of the ContactMessage model
        self.assertEqual(self.contact_message.name, "John Doe")

    def test_contact_message_email(self):
        # Test the email of the ContactMessage model
        self.assertEqual(self.contact_message.email, "john@example.com")

    def test_contact_message_message(self):
        # Test the message of the ContactMessage model
        self.assertEqual(self.contact_message.message, "Hello, this is a test message.")

    def test_contact_message_name_max_length(self):
        # Test the max length of the name field
        max_length = self.contact_message._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_contact_message_email_max_length(self):
        # Test the max length of the email field
        max_length = self.contact_message._meta.get_field('email').max_length
        self.assertEqual(max_length, 254)

    def test_contact_message_name_blank(self):
        # Test the blank attribute of the name field
        blank = self.contact_message._meta.get_field('name').blank
        self.assertEqual(blank, False)

    def test_contact_message_email_blank(self):
        # Test the blank attribute of the email field
        blank = self.contact_message._meta.get_field('email').blank
        self.assertEqual(blank, False)

    def test_contact_message_message_blank(self):
        # Test the blank attribute of the message field
        blank = self.contact_message._meta.get_field('message').blank
        self.assertEqual(blank, False)
