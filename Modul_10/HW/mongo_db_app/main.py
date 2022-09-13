from HW.mongo_db_app.src.app.adressbook import main as ab_main
from HW.mongo_db_app.src.app.notebook import main as note_book


def main():
    while True:
        print('Menu:',
              '1. AddressBook',
              '2. NoteBook',
              '3. Close program', sep='\n')
        user_command = input('Press menu button: >>> ')
        if user_command == '1':
            print('*'*60, 'AddressBook Manager', '*'*60, sep='\n')
            result = ab_main()
            if result == 'Exit':
                continue

        elif user_command == '2':
            print('*' * 60, 'NoteBook Manager: ', '*' * 60, sep='\n')
            result = note_book()
            if result == 'Exit':
                continue

        elif user_command == '3':
            print('Good bye!')
            break


if __name__ == '__main__':
    main()
