# test_calculadora.py
import pytest
from calculadora import somar, subtrair

def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0

def test_subtrair():
    assert subtrair(5, 3) == 2
    assert subtrair(1, 1) == 0
