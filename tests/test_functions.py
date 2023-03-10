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
    assert isinstance(functions.executed_operations(), list)
    assert functions.executed_operations() is not None


def test_sorted_to_data(words):
    """
    Тест функции сортировки по дате(сверху самые последние)
    """
    executed_operations = functions.executed_operations()
    assert isinstance(functions.sorted_data(), list)
    assert functions.sorted_data() != executed_operations


def test_last_operations():
    """
    Тест функции определения последних 5 операций
    """
    sorted = functions.last_operations()
    assert len(sorted[:5]) == 5
    assert isinstance(sorted[:5], list)


def test_hiding_card():
    """
    Тест частичного скрытия карты и счета
    """
    last_five_operations = functions.last_operations()[:5]
    assert isinstance(functions.hiding_card(last_five_operations), list)
    for k in last_five_operations:
        assert isinstance(k, dict)


def test_date_new():
    """
    Тест функции корректировки вывода даты в нужном формате
    """
    last_five_operations = functions.last_operations()[:5]
    assert isinstance(functions.date_new(last_five_operations), list)


def test_conclusion_result():
    """
    Тест функции вывода
    """
    last_five_operations = functions.last_operations()[:5]
    assert functions.conclusion_result(last_five_operations) is True


