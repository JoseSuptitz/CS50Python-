from project import get_guess, check, new_lives

def test_get_guess(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 1000)
    assert get_guess() == 1000
    
def test_check():
    assert check(1000, 500) == True
    assert check(100, 500) == True

def test_new_lives():
    assert new_lives(50) == True