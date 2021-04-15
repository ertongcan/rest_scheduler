from django.test import SimpleTestCase


class ViewsTestCase(SimpleTestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('https://perdoo-case-study.herokuapp.com/admin')
        self.assertEqual(response.status_code, 200)