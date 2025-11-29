import pytest

@pytest.fixture
def sample_numbers():
    return [1, 2, 3, 4]

@pytest.fixture
def sample_text():
    return "hello"
