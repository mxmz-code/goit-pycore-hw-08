import pickle

class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)
        print(f"Запис '{record}' успішно додано.")

    def show_records(self):
        for record in self.records:
            print(record)

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)
    print(f"Адресна книга збережена в {filename}")

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print(f"Не знайдено збережених даних, починаємо з порожньої адресної книги.")
        return AddressBook()
