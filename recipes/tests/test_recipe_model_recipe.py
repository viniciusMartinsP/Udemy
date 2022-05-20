from select import select

from django.core.exceptions import ValidationError
from django.forms import ValidationError
from parameterized import parameterized, parameterized_class

from .test_recipe_base import Recipe, RecipeTestBase


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def make_recipe_no_defaults(self):
        recipe=Recipe(
            category = self.make_category(name='Test default category'),
            author = self.make_author(username='newusername'),
            title = 'Recipe Title',
            description='Recipe Description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe preparation steps',
        )
        recipe.full_clean()
        recipe.save()
        return recipe

    @parameterized.expand([
        ('title',65),
        ('description',165),
        ('preparation_time_unit',65),
        ('servings_unit',65),
    ])

    def test_recipe_fields_max_lenght(self,field, max_length):
        setattr(self.recipe, field, 'A'* (max_length+1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe= self.make_recipe_no_defaults()
        recipe.full_clean()
        recipe.save()
        self.assertFalse(recipe.preparation_steps_is_html, msg='Recipe steps is not false')

    def test_recipe_is_published_is_false_by_default(self):
        recipe= self.make_recipe_no_defaults()
        recipe.full_clean()
        recipe.save()
        self.assertFalse(recipe.is_published, msg='Recipe is published is not false')

    def test_recipe_string_representation(self):
        self.recipe.title = 'Testing recipe tittle'
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(self.recipe.title, 'Testing recipe tittle', msg='O que eu passei, é igual ao que é salvo?' )
