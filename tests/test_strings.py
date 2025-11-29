from app import shout

def test_shout_uppercase():
    assert shout("hello") == "HELLO"

def test_shout_with_fixture(sample_text):
    assert shout(sample_text) == "HELLO"
