from addressbook import AddressBook, save_data, load_data

def interactive_menu():
    print("Ласкаво просимо до програми Адресна книга!")
    print("Виберіть опцію:")
    print("1. Додати запис")
    print("2. Показати всі записи")
    print("3. Зберегти та вийти")

def main():
    addressbook = load_data("addressbook.pkl")
    
    while True:
        interactive_menu()
        choice = input("Введіть ваш вибір: ")
        
        if choice == '1':
            record = input("Введіть запис для додавання: ")
            addressbook.add_record(record)
        elif choice == '2':
            print("Показую всі записи:")
            addressbook.show_records()
        elif choice == '3':
            save_data(addressbook, "addressbook.pkl")
            print("Вихід з програми. Адресна книга збережена.")
            break
        else:
            print("Неправильна опція. Будь ласка, виберіть знову.")

if __name__ == "__main__":
    main()
