from django.test import TestCase, Client
from django.urls import reverse
from django.shortcuts import render


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_handler404(self):
        response = self.client.get('/invalid/url/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'errors/404.html')
