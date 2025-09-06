from praktikum.bun import Bun
import data

import pytest

class TestBun:
    @pytest.mark.parametrize('name, price', data.BUN)
    def test_get_bun_name_return_current_bun_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price', data.BUN)
    def test_get_bun_price_return_current_bun_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price