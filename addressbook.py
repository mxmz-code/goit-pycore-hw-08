import pickle
from datetime import datetime

class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def show_records(self):
        for record in self.records:
            print(record)

    def find_record(self, name):
        found = False
        for record in self.records:
            if name in record:
                print(f"Знайдено запис: {record}")
                found = True
        if not found:
            print(f"Запис для {name} не знайдено.")

    def delete_record(self, name):
        self.records = [record for record in self.records if name not in record]
        print(f"Запис для {name} видалено.")

    def update_record(self, name):
        for i, record in enumerate(self.records):
            if name in record:
                new_name = input(f"Введіть нове ім'я для {name}: ")
                new_phone = input("Введіть новий телефон: ")
                new_birthday = input("Введіть нову дату народження (дд.мм.рррр): ")
                self.records[i] = f"{new_name}, {new_phone}, {new_birthday}"
                print(f"Запис для {name} оновлено.")
                return
        print(f"Запис для {name} не знайдено.")

    def show_upcoming_birthdays(self):
        today = datetime.now()
        upcoming_birthdays = []

        for record in self.records:
            try:
                name, phone, birthday = record.split(", ")
                birth_date = datetime.strptime(birthday, '%d.%m.%Y').replace(year=today.year)

                if birth_date < today:
                    birth_date = birth_date.replace(year=today.year + 1)

                days_until_birthday = (birth_date - today).days
                if days_until_birthday <= 30:
                    upcoming_birthdays.append((name, birthday, days_until_birthday))

            except ValueError:
                print(f"Помилка в форматі дати народження для запису: {record}")

        if upcoming_birthdays:
            print("╔════════════════════════════════╗")
            print("║ Найближчі дні народження:      ║")
            print("╚════════════════════════════════╝")
            for name, birthday, days in sorted(upcoming_birthdays, key=lambda x: x[2]):
                print(f"Ім'я: {name}, День народження: {birthday} (через {days} днів)")
        else:
            print("Немає днів народження в найближчі 30 днів.")

# Функції для збереження та завантаження даних за допомогою pickle
def save_data(addressbook, filename="addressbook.pkl"):
    with open(filename, 'wb') as f:
        pickle.dump(addressbook.records, f)
    print("Адресна книга збережена у файлі addressbook.pkl.")

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, 'rb') as f:
            records = pickle.load(f)
        addressbook = AddressBook()
        addressbook.records = records
        print("Адресна книга завантажена з файлу addressbook.pkl.")
        return addressbook
    except FileNotFoundError:
        print("Файл не знайдено. Створюється нова адресна книга.")
        return AddressBook()
