from app import add, multiply

def test_addition():
    assert add(1, 2) == 3

def test_multiplication():
    assert multiply(3, 4) == 12

def test_sum_with_fixture(sample_numbers):
    assert add(sample_numbers[0], sample_numbers[3]) == 5
