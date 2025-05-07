import pytest
from .. import main

# @pytest.
def test_square():
    assert(main.square(5)==25)

def test_square1():
    assert(not(main.square(3)==25))

def test_square2():
    assert(main.square(4)==25)

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        res = main.divide(4,0)