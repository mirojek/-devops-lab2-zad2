from src.myapp.app import welcome

def test_dummy():
    assert True

def test_welcome():
    result = welcome()
    assert "Witaj" in result