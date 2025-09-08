import pytest
from praktikum.ingredient import Ingredient
import data


class TestIngredient:
    """
    Юнит-тесты для класса Ingredient.
    """
    """Тест проверяет создание ингредиентов с разными параметрами."""

    @pytest.mark.parametrize("ingredient_type, name, price", data.INGREDIENTS)
    def test_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type, name, price", data.INGREDIENTS)
    def test_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize("ingredient_type, name, price", data.INGREDIENTS)
    def test_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
