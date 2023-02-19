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

def sorted_date(executed_operations_list):
    """
    Функция сортировки по дате(сверху самые последние)
    """
    sort_list = sorted(executed_operations_list, key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    return sort_list


def main():
    words = load_words()
    executed_operations_list = executed_operations(words)
    print(sorted_date(executed_operations_list))