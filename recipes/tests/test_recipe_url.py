from audioop import reverse
from pydoc import resolve
from turtle import home

from django.test import TestCase
from django.urls import resolve, reverse
from nturl2path import url2pathname
from recipes import views


class RecipeURLsTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')
    
    def test_recipe_category_url_is_ok(self):
        url = reverse('recipes:category', kwargs={'category_id':2})
        self.assertEqual(url, '/recipes/category/2/')

    def test_recipe_detail_url_is_ok(self):
        url = reverse('recipes:recipe', kwargs={'id':3})
        self.assertEqual(url, '/recipes/3/')
