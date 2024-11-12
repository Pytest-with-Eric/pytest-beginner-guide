import pytest
from app import add, subtract, login


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (5, 3, 8), (-1, -1, -2)])
def test_add(a, b, expected):
    assert add(a, b) == expected


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 5) == 5


def test_login_success():
    assert login("admin", "secret") == "Login successful"


def test_login_failure():
    assert login("user", "wrongpass") == "Invalid credentials"
