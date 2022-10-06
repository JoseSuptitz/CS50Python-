from working import convert
import pytest

def test_AM():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'

def test_PM():
    assert convert('10 PM to 8 AM') == '22:00 to 08:00'
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'

def test_value_error():
    with pytest.raises(ValueError):
        convert('9:70 AM to 5:80 PM')
def test_value_error_2():
    with pytest.raises(ValueError):
        convert('17:00 AM to 16:00 PM')
def test_value_error_for_60():
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:60 PM')
def test_value_error_3():
    with pytest.raises(ValueError):
        convert('9AM to 5PM')
def test_value_error_4():
    with pytest.raises(ValueError):
        convert('10:7 AM - 5:1 PM')
def test_omit_to():
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')
def test_omit_to_two():
    with pytest.raises(ValueError):
        convert('09:00 AM - 17:00 PM')
def test_invalid_input():
        with pytest.raises(ValueError):
            convert('09 AM - 17:00 PM')


