import pytest

from helicopter.generate import string_gen

def test_string_gen():
    assert  type(string_gen()) == str
    assert len(string_gen()) == 5
    assert string_gen().islower