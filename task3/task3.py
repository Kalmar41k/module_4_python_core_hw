"""
Скрипт, який приймає, шлях до директорії, як аргумент, та виводить у консоль піддиректорії 
та файли у вказаній директорії, відокремленими за допомогою кольорів (папка: синій, файл: зелений)
"""
import sys
from processing import log_error, visualize_directory_structure

def main():
    """
    Головна функція програми, що обробляє аргументи командного рядка та викликає функцію для 
    візуалізації структури директорії.

    Вона перевіряє, чи передано правильну кількість аргументів:

        Якщо передано один аргумент (шлях до директорії), викликає функцію 
        visualize_directory_structure(dir_path).

        Якщо аргументи не відповідають умовам, викликає функцію log_error для виведення 
        повідомлення про помилку.
    """
    if 1 < len(sys.argv) < 3:
        dir_path = sys.argv[1]
        visualize_directory_structure(dir_path)
    else:
        log_error("Вкажіть шлях до директорії як аргумент.")

if __name__ == "__main__":
    main()