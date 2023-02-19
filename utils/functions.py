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


def last_operations(sort_list):
    """
    Функция определения последних 5 операций
    """
    return sort_list[:5]


def hiding_card(last_five_operations):
    """
    Частичное скрытие карты и счета
    """
    for k in last_five_operations:
        if 'перевод' in k['description'].lower():
            str = k['from']    #крываем номер карты отправителя
            strlength = len(str)
            masked = strlength - 4
            start_str = str[:masked - 6]
            end_str = str[masked:]
            mask_from = start_str + "*" * 6 + end_str
            str = k['to']    #Скрываем номер карты получателя
            strlength = len(str)
            masked = strlength - 4
            slimstr = str[masked:]
            mask_to = "*" * 2 + slimstr
            k['from'] = mask_from
            k['to'] = mask_to
            dt = datetime.datetime.strptime(k['date'], "%Y-%m-%dT%H:%M:%S.%f")    #Делаем сокращенным время
            new_format = dt.strftime("%d.%m.%Y")
            k['date'] = new_format
        else:
            str = k['to']    #Скрываем номер карты получателя
            strlength = len(str)
            masked = strlength - 4
            start_str = str[:masked - 16]
            end_str = str[masked:]
            mask_to = start_str + "*" * 2 + end_str
            k['to'] = mask_to
            dt = datetime.datetime.strptime(k['date'], "%Y-%m-%dT%H:%M:%S.%f")    #Делаем сокращенным время
            new_format = dt.strftime("%d.%m.%Y")
            k['date'] = new_format
    return last_five_operations



def main():
    words = load_words()
    executed_operations_list = executed_operations(words)
    sort_list = sorted_data(executed_operations_list)
    last_five_operations = last_operations(sort_list)
    for w in hiding_card(last_five_operations):
        print(w)