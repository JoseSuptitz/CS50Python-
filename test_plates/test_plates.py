from plates import is_valid

def test_plates():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False

def test_last_letter():
    assert is_valid('CS50P') == False

def test_punctuation():
    assert is_valid('PI3.14') == False
    assert is_valid('PI4!15') == False

def test_letters():
    assert is_valid('H') == False
    assert is_valid('OUTATIME') == False
    assert is_valid('1234') == False