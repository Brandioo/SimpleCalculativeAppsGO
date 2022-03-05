from findList import *


def test_find_function():
    result = find_in_list(7, [1, 2, 4])
    assert type(result) == bool
    assert result == False

    result = find_in_list(8, [1, 2, 3, 8])
    assert type(result) == bool
    assert result == True

    result = find_in_list("anna", ["anna", "ben"])
    assert result == True

    result = find_in_list(1, [])
    assert result == False
