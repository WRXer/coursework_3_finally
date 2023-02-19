from utils import functions
import requests
import pytest

@pytest.fixture
def words():
    response = requests.get("https://api.npoint.io/ce6d4e606f2fd82a0d68")
    words = response.json()
    return words


def test_load_words(words):
    """
    Тест функции загрузки файла из джсон
    """
    assert type(functions.load_words()) == type(words)
    assert functions.load_words() is not None


def test_executed_operations(words):
    """
    Тест функции отбора выполненных операций
    """
    assert type(functions.executed_operations(words)) == list
    assert functions.executed_operations(words) is not None


def test_sorted_to_date()