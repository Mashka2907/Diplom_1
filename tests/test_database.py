from praktikum.database import Database


class TestDatabase:
    """
    Юнит-тесты для класса Database.
    """

    def test_database_available_buns(self):
        db = Database()
        available_buns = db.available_buns()

        assert len(available_buns) == 3
        assert isinstance(available_buns, list)

    def test_database_available_ingredients(self):
        db = Database()
        available_ingredients = db.available_ingredients()

        assert len(available_ingredients) == 6
        assert isinstance(available_ingredients, list)