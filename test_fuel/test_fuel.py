from fuel import convert, gauge
import pytest

def test_convert():
    assert convert('3/4') == 75
    assert convert('1/4') == 25

def test_gauge():
    assert gauge(99) == 'F'
    assert gauge(1) == 'E'
    assert gauge(50) == '50%'

def test_errors():
    with pytest.raises(ValueError):
        convert('5/4')
    with pytest.raises(ValueError):
        convert('X/Y')
    with pytest.raises(ZeroDivisionError):
        convert('5/0')