import pytest 
from QA-Challenges import adding

def test_one():
    input = str(9)
    isinstance(adding.adder(input), int)
    return True