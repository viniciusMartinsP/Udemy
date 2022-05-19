from audioop import reverse
from pydoc import resolve

from django.test import TestCase
from django.urls import resolve, reverse
from recipes import views


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

    def test_recipe_view_status_code_200_is_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIs(response.status_code, 200)
    
    def test_recipe_view_template_is_correct(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')
