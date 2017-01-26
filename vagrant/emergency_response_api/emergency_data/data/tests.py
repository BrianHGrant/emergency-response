from django.test import TestCase
from data.models import Agency
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
class AgencyTests(APITestCase):
    def test_get_agency(self):
        """
        Ensure we can get a agency object
        """
        response = self.client.get('agencies/4/')
        self.assertEqual(response.data, {'id': 4})
