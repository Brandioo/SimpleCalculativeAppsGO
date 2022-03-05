import pytest

from age_tools import calc_age


def test_calculate_age():
    assert calc_age(65) == 23725
    assert calc_age(0) == 0
    assert calc_age(20) == 7300
    assert calc_age(-300) == 0
    assert calc_age(1.5) == 730
    # assert calc_age("n") == 0
    # assert calc_age([1, 2, 3]) == 0


def test_calculate_age_errors():
    with pytest.raises(TypeError):
        calc_age("N")
    with pytest.raises(TypeError):
        calc_age([1, 2, 3])
