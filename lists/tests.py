from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import lists_home
from lists.models import Item


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/lists/')
        self.assertTemplateUsed(response, 'lists/lists_home.html')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/lists/')
        self.assertEqual(Item.objects.count(), 0)

    def test_can_save_a_POST_request(self):
        self.client.post('/lists/', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/lists/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/')

    def test_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/lists/')

        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 1', response.content.decode())
