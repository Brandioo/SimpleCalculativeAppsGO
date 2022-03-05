import pytest

from multiples import *

def test_list_of_multiples2():
    resulta = list_of_multiples_version2(7, 5)
    assert type(resulta) == list
    assert len(resulta) == 5
    assert resulta == [7, 14, 21, 28, 35]

    assert list_of_multiples_version2(12, 10) == [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
    with pytest.raises(TypeError):
        assert list_of_multiples_version2(17, 6.0)

    with pytest.raises(ValueError):
        assert list_of_multiples_version2(17, -1)

    with pytest.raises(ValueError):
        assert list_of_multiples_version2(17, 0)