from unittest.mock import Mock
import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
import data


class TestBurger:
    """
    Юнит-тесты для класса Burger.
    """
    def test_set_buns(self):
        """Тест установки булочек"""
        burger = Burger()
        bun = Bun("Wheat Bun", 1.5)
        burger.set_buns(bun)

        assert burger.bun == bun

    @pytest.mark.parametrize("ingredient_type, name, price", data.INGREDIENTS)
    def test_add_ingredient(self, ingredient_type, name, price):
        """Тест добавления ингредиента"""
        burger = Burger()
        ingredient = Ingredient(ingredient_type, name, price)
        burger.add_ingredient(ingredient)

        assert ingredient in burger.ingredients

    @pytest.mark.parametrize("ingredient_type, name, price", data.INGREDIENTS)
    def test_remove_ingredient(self, ingredient_type, name, price):
        """Тест удаления ингредиента"""
        burger = Burger()
        ingredient = Ingredient(ingredient_type, name, price)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_move_ingredient(self):
        """Тест перемещения ингредиента"""
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == mock_ingredient_2
        assert burger.ingredients[1] == mock_ingredient_1

    def test_get_price_no_ingredients(self):
        """Тест получения цены без ингредиентов"""
        burger = Burger()
        bun = Bun("Wheat Bun", 1.5)
        burger.set_buns(bun)

        # Цена должна быть равна удвоенной цене булочки, так как их две
        assert burger.get_price() == 3.0

    def test_get_price_with_ingredients(self):
        """Тест получения цены с ингредиентами"""
        burger = Burger()
        bun = Bun("Wheat Bun", 1.5)
        burger.set_buns(bun)
        ingredient1 = Ingredient("filling", "Cheese", 1.0)
        ingredient2 = Ingredient("sauce", "Ketchup", 0.5)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        # Цена: 2 * 1.5 (булочки) + 1.0 (сыр) + 0.5 (кетчуп) = 4.5
        assert burger.get_price() == 4.5

    def test_get_receipt(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = data.BUN[0][0]
        mock_bun.get_price.return_value = data.BUN[0][1]
        burger.bun = mock_bun

        mock_ingredient1 = Mock()
        mock_ingredient1.get_name.return_value = data.INGREDIENTS[0][1]
        mock_ingredient1.get_type.return_value = 'соусы'
        mock_ingredient1.get_price.return_value = data.INGREDIENTS[0][2]

        mock_ingredient2 = Mock()
        mock_ingredient2.get_name.return_value = data.INGREDIENTS[5][1]
        mock_ingredient2.get_type.return_value = 'начинки'
        mock_ingredient2.get_price.return_value = data.INGREDIENTS[5][2]

        mock_ingredient3 = Mock()
        mock_ingredient3.get_name.return_value = data.INGREDIENTS[7][1]
        mock_ingredient3.get_type.return_value = 'начинки'
        mock_ingredient3.get_price.return_value = data.INGREDIENTS[7][2]

        burger.ingredients = [mock_ingredient1, mock_ingredient2, mock_ingredient3]
        expected_receipt = "(==== pretty bun ====)\n= соусы Соус Spicy-X =\n= начинки Говяжий метеорит (отбивная) =\n= начинки Филе Люминесцентного тетраодонтимформа =\n(==== pretty bun ====)\nPrice: 4476"
        receipt_text = burger.get_receipt().replace("\n\n", "\n")

        assert receipt_text == expected_receipt

