from addressbook import AddressBook, save_data, load_data
from utils import print_menu, get_input

def interactive_menu():
    print_menu()

def main():
    addressbook = load_data("addressbook.pkl")

    while True:
        interactive_menu()
        choice = get_input("╔════════════════════════════════╗\n║ Введіть ваш вибір:             ║\n╚════════════════════════════════╝\n")
        
        if choice == '1':
            record = get_input("\n╔════════════════════════════════╗\n║ Введіть запис для додавання:   ║\n╚════════════════════════════════╝\n")
            addressbook.add_record(record)
            print("\n╔════════════════════════════════╗\n║ Запис додано успішно!          ║\n╚════════════════════════════════╝\n")
        elif choice == '2':
            print("\n╔════════════════════════════════╗\n║ Показую всі записи:            ║\n╚════════════════════════════════╝\n")
            addressbook.show_records()
            print("\n")
        elif choice == '3':
            search_term = get_input("\n╔════════════════════════════════╗\n║ Введіть ім'я для пошуку:       ║\n╚════════════════════════════════╝\n")
            addressbook.find_record(search_term)
        elif choice == '4':
            record_to_delete = get_input("\n╔════════════════════════════════╗\n║ Введіть ім'я для видалення:    ║\n╚════════════════════════════════╝\n")
            addressbook.delete_record(record_to_delete)
        elif choice == '5':
            record_to_update = get_input("\n╔════════════════════════════════╗\n║ Введіть ім'я для оновлення:    ║\n╚════════════════════════════════╝\n")
            addressbook.update_record(record_to_update)
        elif choice == '6':
            print("\n╔════════════════════════════════╗\n║ Найближчі дні народження:      ║\n╚════════════════════════════════╝\n")
            addressbook.show_upcoming_birthdays()
        elif choice == '7':
            save_data(addressbook, "addressbook.pkl")
            print("\n╔════════════════════════════════╗\n║ Адресна книга збережена.       ║\n╚════════════════════════════════╝\n")
        elif choice == '8':
            save_data(addressbook, "addressbook.pkl")
            print("\n╔════════════════════════════════╗\n║ Вихід з програми.              ║\n╚════════════════════════════════╝\n")
            break
        else:
            print("\n╔════════════════════════════════╗\n║ Неправильна опція.             ║\n║ Будь ласка, виберіть знову.    ║\n╚════════════════════════════════╝\n")

if __name__ == "__main__":
    main()
