"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    list_repres = [
        {'name':'Вася', 'age':'30', 'job':'Программист'},
        {'name':'Петя', 'age':'45', 'job':'Сантехник'},
        {'name':'Маша', 'age':'25', 'job':'Учитель'},
        {'name':'Катя', 'age':'20', 'job':'Дизайнер'},
        {'name':'Лёва', 'age':'30', 'job':'Дворник'}
    ]

    import csv

    with open('represent.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        represent = csv.DictWriter(f, fields, delimiter=';')
        represent.writeheader()

        for person in list_repres:
            represent.writerow(person)

if __name__ == "__main__":
    main()
