import pytest
from app import add

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 1, 2),
        (2, 3, 5),
        (-1, 5, 4),
        (10, -3, 7),
    ]
)
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected
