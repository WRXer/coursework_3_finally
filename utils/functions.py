import requests
import datetime

def load_words():
    """
    Функция преобразования файла из джсон
    """
    file = requests.get("https://api.npoint.io/ce6d4e606f2fd82a0d68")
    words = file.json()
    return words


def executed_operations(words):
    """
    Функция отбора выполненных операций
    """
    executed_operations_list = []
    for w in words:
        if not w:  # Ищем пустые словари
            continue
        else:
            if w['state'].lower() == "executed":  # Условие, что операция выполнена
                executed_operations_list.append(w)
    return executed_operations_list

def sorted_data(executed_operations_list):
    """
    Функция сортировки по дате(сверху самые последние)
    """
    return sorted(executed_operations_list, key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)


def main():
    words = load_words()
    executed_operations_list = executed_operations(words)
    sort_list = sorted_data(executed_operations_list)