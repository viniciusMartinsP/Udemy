from audioop import reverse
from pydoc import resolve
from turtle import home

from django.test import TestCase
from django.urls import resolve, reverse
from nturl2path import url2pathname

from recipes import views


# Create your tests here.
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

class RecipeViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id':2}))
        self.assertIs(view.func, views.category)
        
    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id':3}))
        self.assertIs(view.func, views.recipe)
