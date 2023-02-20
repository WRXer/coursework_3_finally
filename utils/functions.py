import requests
import datetime

def load_words():
    """
    Функция преобразования файла из джсон
    """
    file = requests.get("https://api.npoint.io/ce6d4e606f2fd82a0d68")
    words = file.json()
    return words


def executed_operations():
    """
    Функция отбора выполненных операций
    """
    words = load_words()
    executed_operations_list = []
    for w in words:
        if not w:  # Ищем пустые словари
            continue
        else:
            if w['state'].lower() == "executed":  # Условие, что операция выполнена
                executed_operations_list.append(w)
    return executed_operations_list

def sorted_data():
    """
    Функция сортировки по дате(сверху самые последние)
    """
    executed_operations_list = executed_operations()
    return sorted(executed_operations_list, key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)


def last_operations():
    """
    Функция определения последних 5 операций
    """
    sort_list = sorted_data()
    return sort_list[:5]


def hiding_card(last_five_operations):
    """
    Частичное скрытие карты и счета
    """
    for k in last_five_operations:
        if 'перевод' in k['description'].lower():
            if 'счет' in k['from'].lower():
                k['from'] = k['from'][:(len(k['from']) - 4) - 10] + '*' * 6 + k['from'][(len(k['from']) - 4):]
            k['from'] = k['from'][:(len(k['from']) - 4)-6] + '*' * 6 + k['from'][(len(k['from']) - 4):]    #Cкрываем номер карты отправителя
        k['to']  = k['to'][:(len(k['to']) - 4) - 16] + '*' * 2 + k['to'][(len(k['to']) - 4):]    # Скрываем номер карты получателя
    return last_five_operations


def date_new(last_five_operations):
    """
    Функция корректировки вывода даты в нужном формате
    """
    hiding_card(last_five_operations)
    for k in last_five_operations:
        k['date'] = (datetime.datetime.strptime(k['date'], "%Y-%m-%dT%H:%M:%S.%f")).strftime("%d.%m.%Y")  # Делаем сокращенным время
    return last_five_operations


def conclusion_result(last_five_operations):
    """
    Функция вывода
    """
    date_new(last_five_operations)
    for w in last_five_operations:
        if 'перевод' in w['description'].lower():
            print(f"{w['date']} {w['description']}\n{w['from']} -> {w['to']}\n{w['operationAmount']['amount']} {w['operationAmount']['currency']['name']} \n ")
        else:
            print(f"{w['date']} {w['description']}\n{w['to']}\n{w['operationAmount']['amount']} {w['operationAmount']['currency']['name']} \n ")
    return True


def main():
    last_five_operations = last_operations()
    conclusion_result(last_five_operations)