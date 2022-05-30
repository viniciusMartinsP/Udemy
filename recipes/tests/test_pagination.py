from multiprocessing.pool import AsyncResult

from django.core import paginator
from django.test import TestCase
from django.urls import resolve, reverse
from recipes.tests.test_recipe_base import RecipeTestBase


class PaginationTestBase(RecipeTestBase):
    def test_if_pagination_is_correctly_loading_all_itens(self):
        for i in range(9):
            kwargs = {'slug':f'slug-{i}', 'author_data':{'username':f'user{i}'}}
            self.make_recipe(**kwargs)
        response = self.client.get(reverse('recipes:home'))
        recipes = response.context['recipes']
        paginator = recipes.paginator

        self.assertEqual(paginator.num_pages, 1)

        with self.assertRaises(AssertionError):
            self.assertEqual(paginator.num_pages, 2)

    def test_if_make_pagination_except_value_current_page_is_1(self):
        for i in range(50):
            kwargs = {'slug':f'slug-{i}', 'author_data':{'username':f'user{i}'}}
            self.make_recipe(**kwargs)
        response = self.client.get(reverse('recipes:home'))
        recipes = response.context['recipes']
        paginator = recipes.paginator
        self.assertEqual(recipes.start_index(),1)






