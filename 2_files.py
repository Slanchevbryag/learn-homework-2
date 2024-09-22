"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    filename = 'referat.txt'
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.read() 

    len_str = len(lines)
    print(f'Длина получившейся строки {len_str} символов')

    word = lines.split()
    quan_word = len(word)
    print(f'В этом тексте {quan_word} слова')

    new_lines = lines.replace('.', '!')
    
    with open('referar2.txt', 'w', encoding='utf-8') as new_f:
        new_f.write(new_lines)

if __name__ == "__main__":
    main()
