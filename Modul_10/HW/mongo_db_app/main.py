from HW.mongo_db_app.src.adressbook import main as ab_main


def main():
    while True:
        print('Menu:',
              '1. AddressBook',
              '2. Close program', sep='\n')
        user_command = input('Press menu button: >>> ')
        if user_command == '1':
            print('*'*60, 'AddressBook Manager', '*'*60, sep='\n')
            result = ab_main()
            if result == 'Exit':
                continue
        elif user_command == '2':
            print('Good bye!')
            break


if __name__ == '__main__':
    main()
