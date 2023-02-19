from utils import functions
import requests


def test_load_words():
    """
    Тест функции загрузки файла из джсон
    """
    response = requests.get("https://api.npoint.io/ce6d4e606f2fd82a0d68")
    file = response.json()
    assert type(functions.load_words()) == type(file)
    assert functions.load_words() is not None