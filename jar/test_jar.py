from jar import Jar
import pytest

def test_init_():
    jar = Jar()
    assert jar.capacity == 12

def test_str_():
    jar = Jar()
    jar.deposit(6)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪'

def test_deposit_():
    jar = Jar()
    jar.deposit(6)
    assert jar.size == 6

def test_withdraw_():
    jar = Jar()
    jar.deposit(6)
    jar.withdraw(3)
    assert jar.size == 3

def test_value_error():
    jar = Jar()
    jar.deposit(6)
    with pytest.raises(ValueError):
        jar.withdraw(7)