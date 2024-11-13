import pytest
from app import add, subtract, login


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (5, 3, 8)])
def test_add_param(a, b, expected):
    assert add(a, b) == expected


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 5) == 5


@pytest.mark.slow
def test_add_large_numbers():
    assert add(1000, 2000) == 3000


def test_add_with_fixture(sample_data):
    result = add(sample_data["a"], sample_data["b"])
    assert result == 5


def test_empty_username():
    with pytest.raises(ValueError, match="Username cannot be empty."):
        login("", "password123")


def test_short_password():
    with pytest.raises(
        ValueError, match="Password must be at least 6 characters long."
    ):
        login("user", "123")
