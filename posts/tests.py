from django.test import TestCase
from django.test import SimpleTestCase
from django.core.paginator import Paginator
from django.urls import reverse

# class PaginationTemplateTest(SimpleTestCase):
#     def test_pagination_links(self):
#         # Create a Paginator instance with sample data
#         data = ['item1', 'item2', 'item3', 'item4', 'item5']
#         paginator = Paginator(data, 2)
#
#         # Get the first page of data
#         page = paginator.get_page(1)
#
#         # Render the pagination template with the page
#         response = self.client.get(reverse('pagination'), {'page': page.number})  # Replace 'pagination' with the actual URL name
#
#         # Check if pagination links are present in the response
#         self.assertContains(response, '&laquo; first', count=1)
#         self.assertContains(response, 'previous', count=1)
#         self.assertContains(response, '1', count=1)
#         self.assertContains(response, '2', count=1)
#         self.assertContains(response, 'next', count=1)
#         self.assertContains(response, 'last &raquo;', count=1)