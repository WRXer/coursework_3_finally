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
    assert isinstance(functions.executed_operations(words), list)
    #assert type(functions.executed_operations(words)) == list
    assert functions.executed_operations(words) is not None


def test_sorted_to_data(words):
    """
    Тест функции сортировки по дате(сверху самые последние)
    """
    executed_operations = functions.executed_operations(words)
    assert isinstance(functions.sorted_data(executed_operations), list)
    assert functions.sorted_data(executed_operations) != executed_operations


def test_last_operations(words):
    """
    Тест функции определения последних 5 операций
    """
    sorted = functions.last_operations(functions.sorted_data(functions.executed_operations(words)))
    assert len(sorted[:5]) == 5
    assert isinstance(sorted[:5], list)


def hiding_card(last_five_operations):
    """
    Тест частичного скрытия карты и счета
    """
    pass