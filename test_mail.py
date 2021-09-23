import pytest

# int 

@pytest.mark.parametrize("x, x_abs", [ (-1, 1), (0, 0), (1, 1)] )
def test_abs(x, x_abs):
    assert abs(x) == x_abs

# Negative test
def test_degree():
    try:
        assert [2**2, 4**2, 3**2] == [4, 16, 6]
    except AssertionError:
        pass

def test_math():
    assert divmod(16, 3) == (5, 1)


# float

@pytest.mark.parametrize("x, y, z", [ (-3.0, 5.0, -15.0), (0.0, 0.0, 0.0), (3.5, 2.5, 8.75) ])
def test_multiply(x, y, z):
    assert x * y == z

# Negative test
def test_pow():
    try:
        assert pow(5.0, 2.0) == 24.0
    except AssertionError:
        pass

def test_plus():
    assert 5.5 + 3.3 == 8.8
