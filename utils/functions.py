import requests


def load_words():
    """
    Функция преобразования файла из джсон
    """
    file = requests.get("https://api.npoint.io/ce6d4e606f2fd82a0d68")
    words = file.json()
    return words
