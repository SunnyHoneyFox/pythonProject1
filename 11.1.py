import requests


def get_request(url):
    response = requests.get(url)
    return response


def post_request(url, data):
    response = requests.post(url, data=data)
    return response


def get_with_params(url, params):
    response = requests.get(url, params=params)
    return response


def display_response_info(response):
    if response.status_code == 200:
        print("Запрос выполнен успешно!")
    else:
        print(f"Произошла ошибка. Код ответа: {response.status_code}")

    print(f'Заголовки: {response.headers}')
    print(f'Содержимое страницы:\n{response.text[:130]}...')


if __name__ == "__main__":
    url = 'https://www.vokrugsveta.ru'

    print("GET-запрос:")
    response = get_request(url)
    display_response_info(response)

    print("\nPOST-запрос:")
    data = {'title': 'foo', 'body': 'bar', 'userId': 1}
    response = post_request(url, data)
    display_response_info(response)

    print("\nGET-запрос с параметрами:")
    params = {'userId': 1}
    response = get_with_params(url, params)
    display_response_info(response)


import csv

data = [
    ['Name', 'Age', 'Salary'],
    ['Alex', 33, 65000],
    ['Elena', 42, 188000],
    ['Ignat', 35, 96000],
    ['Mariya', 29, 82000],
    ['Pavel', 39, 76000],
    ['Yan', 19, 18900]
]

with open('data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)
# import pandas as pd




df = pd.read_csv('data.csv')


def display_head(dataframe, n=4):
    print("Первые 4 строки данных:")
    print(dataframe.head(n))


def average_salary_and_age(dataframe):
    average_salary = dataframe['Salary'].mean()
    average_age = dataframe['Age'].mean()
    print(f"\nСредняя зарплата: {average_salary:.2f}")
    print(f"Средний возраст: {average_age:.2f}")


def employees_above_average(dataframe):
    average_salary = dataframe['Salary'].mean()
    above_average = dataframe[dataframe['Salary'] > average_salary]
    print("\nСотрудники с зарплатой выше средней:")
    print(above_average)


if __name__ == "__main__":
    display_head(df)

    average_salary_and_age(df)

    employees_above_average(df)


import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Исходный массив:", array)

array_add = array + 10
array_subtract = array - 2
array_multiply = array * 3

print("Массив после сложения 10:", array_add)
print("Массив после вычитания 2:", array_subtract)
print("Массив после умножения на 3:", array_multiply)

sum_value = np.sum(array)
print("Сумма элементов массива:", sum_value)

mean_value = np.mean(array)
print("Среднее значение массива:", mean_value)

squared_array = np.square(array)
print("Массив, возведенный в квадрат:", squared_array)



import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 11, 100)
y1 = np.sin(x)
y2 = np.cos(x)


plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='sin(x)', color='blue')
plt.plot(x, y2, label='cos(x)', color='red')


plt.title('Графики синуса и косинуса')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.7, ls='--')
plt.axvline(0, color='black', linewidth=0.7, ls='--')
plt.grid(color='gray', linestyle='--', linewidth=0.6)
plt.legend()


plt.xlim(0, 11)
plt.ylim(-2, 2)


plt.savefig('sin_cos_plot.png', dpi=300, bbox_inches='tight')


plt.show()
