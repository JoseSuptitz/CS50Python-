from bank import value

def test_HELLO():
    assert value('hello') == 0
    assert value('HeLlO')  == 0

def test_H():
    assert value('heeeey') == 20
    assert value('honaldo') == 20
    assert value('Hoho') == 20

def test_rest():
    assert value('potato man') == 100
    assert value('aa a aa a') == 100
    assert value('AaAaaaAAaa') == 100
