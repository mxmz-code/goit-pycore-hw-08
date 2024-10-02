from datetime import datetime  # Додаємо імпорт модуля datetime

def print_menu():
    print("\n╔════════════════════════════════════════╗")
    print("║              Адресна Книга             ║")
    print("╠════════════════════════════════════════╣")
    print("║ 1. Додати контакт                      ║")
    print("║ 2. Показати всі записи                 ║")
    print("║ 3. Знайти запис                        ║")
    print("║ 4. Видалити запис                      ║")
    print("║ 5. Оновити запис                       ║")
    print("║ 6. Показати найближчі дні народження   ║")
    print("║ 7. Зберегти адресну книгу              ║")
    print("║ 8. Вийти                               ║")
    print("╚════════════════════════════════════════╝\n")

def get_input(prompt):
    return input(prompt)

def validate_name(name):
    return name.isalpha()

def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10

def validate_birthday(birthday):
    try:
        datetime.strptime(birthday, '%d.%m.%Y')  # Перевіряємо формат дати
        return True
    except ValueError:
        return False
