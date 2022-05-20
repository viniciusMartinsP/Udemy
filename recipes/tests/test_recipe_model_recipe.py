from select import select

from django.core.exceptions import ValidationError
from django.forms import ValidationError

from .test_recipe_base import RecipeTestBase


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def test_recipe_title_raises_error_if_title_has_more_than_65_chars(self):
       self.recipe.title = 'A' * 66

#Esse trecho significa que espero que seja levantado uma exceção, caso não seja levantada, haverá um erro 
       with self.assertRaises(ValidationError):
           self.recipe.full_clean()
