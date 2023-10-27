from package_main.main import say_hello

def test_say_hello():
    assert say_hello("Alex") == "Hello, Alex!"
    assert say_hello("") == "Hello, !"