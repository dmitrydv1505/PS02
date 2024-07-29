import requests
import json

def zaдание1():
    # URL для поиска репозиториев с кодом HTML
    url = 'https://api.github.com/search/repositories'

    # Параметры запроса
    params = {
        'q': 'language:html'
    }

    # Отправка GET-запроса
    response = requests.get(url, params=params)

    # Вывод статуса ответа
    print("Статус-код ответа:", response.status_code)

    # Вывод содержимого ответа в формате JSON
    response_json = response.json()
    print("Содержимое ответа в формате JSON:", response_json)

    # Сохранение содержимого ответа в текстовый файл
    with open('Задание1.json', 'w', encoding='utf-8') as file:
        json.dump(response_json, file, ensure_ascii=False, indent=4)

def zaдание2():
    # URL для получения записей пользователя с userId = 1
    url = 'https://jsonplaceholder.typicode.com/posts'

    # Параметры запроса
    params = {
        'userId': 1
    }

    # Отправка GET-запроса
    response = requests.get(url, params=params)

    # Вывод статуса ответа
    print("Статус-код ответа:", response.status_code)

    # Вывод содержимого ответа в формате JSON
    response_json = response.json()
    print("Содержимое ответа в формате JSON:", response_json)

    # Сохранение содержимого ответа в текстовый файл
    with open('Задание2.json', 'w', encoding='utf-8') as file:
        json.dump(response_json, file, ensure_ascii=False, indent=4)

def zaдание3():
    # URL для отправки POST-запроса
    url = 'https://jsonplaceholder.typicode.com/posts'

    # Данные для отправки
    data = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }

    # Отправка POST-запроса
    response = requests.post(url, json=data)

    # Вывод статуса ответа
    print("Статус-код ответа:", response.status_code)

    # Вывод содержимого ответа в формате JSON
    response_json = response.json()
    print("Содержимое ответа в формате JSON:", response_json)

    # Сохранение содержимого ответа в текстовый файл
    with open('Задание3.json', 'w', encoding='utf-8') as file:
        json.dump(response_json, file, ensure_ascii=False, indent=4)
        
# Выбор задания
chosen_task = input("Выберите задание (Задание1, Задание2, Задание3): ")

if chosen_task == "Задание1":
    zaдание1()
elif chosen_task == "Задание2":
    zaдание2()
elif chosen_task == "Задание3":
    zaдание3()
else:
    print("Некорректный выбор задания")