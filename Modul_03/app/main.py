from app.adressbook import main as ab_main
from app.cleanfolder import main as clean_main
from app.notebook import main as note_book


# main функція проекту
def main():
    while True:
        print('Menu:',
              '1. AddressBook',
              '2. NoteBook',
              '3. CleanFolder',
              '4. Close program', sep='\n')
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
            print('*'*60, 'CleanFolder manager', '*'*60, sep='\n')
            result = clean_main()
            if result == 'Exit':
                continue

        elif user_command == '4':
            print('Good bye!')
            break


if __name__ == '__main__':
    main()
