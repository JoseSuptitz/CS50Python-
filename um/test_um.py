from um import count

def test_one():
    assert count('um') == 1
def test_special():
    assert count('um?') == 1
def test_phrase():
    assert count('Um, thanks for the album.') == 1
def test_dots():
    assert count('Um, thanks, um...') == 2

