from src.fibonacci import fibonacci

import pytest


@pytest.mark.parametrize(
    "value,expected",
    [
        (3,2),
        (1,1),
        (5,5),
    ]
)

def test_fibonacci_params(value,expected):
    assert fibonacci(value) == expected