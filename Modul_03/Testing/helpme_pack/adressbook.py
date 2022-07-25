import datetime
import pickle
from collections import UserDict
from datetime import date
import re


class Field:
    def __init__(self, value: str) -> None:
        self.__value = None
        self.value = value

    def __repr__(self) -> str:
        return f'{self.value}'

    def __str__(self) -> str:
        return f'{self.value}'

    def __eq__(self, other) -> bool:
        return self.value == other.value


class Name(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value.title()


class Phone(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        def is_code_valid(phone_code: str) -> bool:
            if phone_code[:2] in ('03', '04', '05', '06', '09') and phone_code[2] != '0' and phone_code != '039':
                return True
            return False

        result = None
        phone = value.removeprefix('+').replace('(', '').replace(')', '').replace('-', '')
        if phone.isdigit():
            if phone.startswith('0') and len(phone) == 10 and is_code_valid(phone[:3]):
                result = '+38' + phone
            if phone.startswith('380') and len(phone) == 12 and is_code_valid(phone[2:5]):
                result = '+' + phone
            if 10 <= len(phone) <= 14 and not phone.startswith('0') and not phone.startswith('380'):
                result = '+' + phone
        if result is None:
            raise ValueError(f'Невірний тип значення {value}')
        self.__value = result


class Birthday(Field):
    def __str__(self):
        if self.value is None:
            return 'Unknown'
        else:
            return f'{self.value:%d %b %Y}'

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        if value is None:
            self.__value = None
        else:
            try:
                self.__value = datetime.datetime.strptime(value, '%d.%m.%Y').date()
            except ValueError:
                print("Enter the date of birth (dd.mm.yyyy)")


class Address(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value.title()


class Email(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        result = None
        get_email = re.findall(r'\b[a-zA-Z][\w\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}', value)
        for i in get_email:
            result = i
        if result is None:
            raise AttributeError(f" Email is not correct {value}")
        self.__value = result


class Record:
    def __init__(self, name: Name, phones=[], birthday=None, email=None, address=None) -> None:
        self.name = name
        self.phone_list = phones
        self.birthday = birthday
        self.address = address
        self.email = email

    def __str__(self) -> str:
        return f' Contact:  {self.name.value.title():20}\n' \
               f' Phones:   {", ".join([phone.value for phone in self.phone_list])}\n' \
               f' Birthday: {self.birthday}\n' \
               f' Email:    {self.email}\n' \
               f' Address:  {self.address}'

    def add_phone(self, phone: Phone) -> None:
        self.phone_list.append(phone)

    def del_phone(self, phone: Phone) -> None:
        self.phone_list.remove(phone)

    def edit_phone(self, phone: Phone, new_phone: Phone) -> None:
        self.phone_list.remove(phone)
        self.phone_list.append(new_phone)

    def days_to_birthday(self, birthday: Birthday):
        if birthday.value is None:
            return None
        this_day = date.today()
        birthday_day = date(this_day.year, birthday.value.month, birthday.value.day)
        if birthday_day < this_day:
            birthday_day = date(this_day.year + 1, birthday.value.month, birthday.value.day)
        return (birthday_day - this_day).days


class AddressBook(UserDict):
    def __init__(self) -> None:
        super().__init__()

    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def iterator(self, func=None, days=0):
        index, print_block = 1, '-' * 50 + '\n'
        for record in self.data.values():
            if func is None or func(record):
                print_block += str(record) + '\n'
                if index < 1:
                    index += 1
                else:
                    yield print_block
                    index, print_block = 1, '-' * 50 + '\n'
        yield print_block


class InputError:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, contacts, *args):
        try:
            return self.func(contacts, *args)
        except IndexError:
            return 'Error! Print correct data!'
        except KeyError:
            return 'Error! User not found!'
        except ValueError:
            return 'Error! Data is incorrect!'
        except AttributeError:
            return "Enter correct the date of birth (dd.mm.yyyy) for this user"


def greeting(*args):
    return 'Hello! How can I help you?'


@InputError
def add_contact(contacts, *args):
    name = Name(args[0])
    phone = Phone(args[1])
    if name.value in contacts:
        if phone in contacts[name.value].phone_list:
            return f'User {name.value.title()} already has this phone'
        else:
            contacts[name.value].add_phone(phone)
            writing_db(contacts)
            return f'Add phone {phone} to user {name.value.title()}'

    else:
        contacts[name.value] = Record(name, [phone])
        writing_db(contacts)
        return f'Add user {name.value.title()} with phone number {phone}'


@InputError
def change_contact(contacts, *args):
    name, old_phone, new_phone = args[0], args[1], args[2]
    contacts[name].edit_phone(Phone(old_phone), Phone(new_phone))
    writing_db(contacts)
    return f'Change to user {name} phone number from {old_phone} to {new_phone}'


@InputError
def show_phone(contacts, *args):
    name = args[0]
    phone = contacts[name]
    return f'{phone}'


@InputError
def del_phone(contacts, *args):
    name, phone = args[0], args[1]
    contacts[name].del_phone(Phone(phone))
    writing_db(contacts)
    return f'Delete phone {phone} from user {name}'


@InputError
def show_all(contacts, *args):
    if not contacts:
        return 'Address book is empty'
    result = 'List of all users:\n'
    print_list = contacts.iterator()
    for item in print_list:
        result += f'{item}'
    return result


@InputError
def add_email(contacts, *args):
    name, email = args[0], args[1]
    contacts[name].email = Email(email)
    writing_db(contacts)
    return f'Add/modify email {contacts[name].email} to user {name}'


@InputError
def add_address(contacts, *args):
    name, address = args[0], list(args[1:])
    address = " ".join(address)
    contacts[name].address = Address(address)
    writing_db(contacts)
    return f'Add/modify address {address.title()} to user {name}'


@InputError
def add_birthday(contacts, *args):
    name, birthday = args[0], args[1]
    contacts[name].birthday = Birthday(birthday)
    writing_db(contacts)
    return f'Add/modify birthday {contacts[name].birthday} to user {name}'


@InputError
def days_to_user_birthday(contacts, *args):
    name = args[0]
    if contacts[name].birthday.value is None:
        return 'User has no birthday'
    return f'{contacts[name].days_to_birthday(contacts[name].birthday)} days to user {name} birthday'


@InputError
def show_birthday_30_days(contacts, *args):
    def func_days(record):
        return record.birthday.value is not None and record.days_to_birthday(record.birthday) <= days

    days = int(args[0])
    result = f'List of users with birthday in {days} days:\n'
    print_list = contacts.iterator(func_days)
    for item in print_list:
        result += f'{item}'
    return result


def exiting(contacts, *args):
    writing_db(contacts)
    return 'Good bye!'


def find(contacts, *args):
    def func_sub(record):
        return substring.lower() in record.name.value.lower() or \
               any(substring in phone.value for phone in record.phone_list)

    substring = args[0]
    result = f'List of users with \'{substring.lower()}\' in data:\n'
    print_list = contacts.iterator(func_sub)
    for item in print_list:
        result += f'{item}'
    return result


@InputError
def del_user(contacts, *args):
    name = args[0]
    yes_no = input(f'Are you sure you want to delete the user {name}? (y/n) ')
    if yes_no == 'y':
        del contacts[name]
        writing_db(contacts)
        return f'Delete user {name}'

    else:
        return 'User not deleted'


@InputError
def clear_all(contacts, *args):
    yes_no = input('Are you sure you want to delete all users? (y/n) ')
    if yes_no == 'y':
        contacts.clear()
        writing_db(contacts)
        return 'Address book is empty'
    else:
        return 'Removal canceled'


def info(*args):
    return """
    *********** Service command ***********
    "help", "?"          --> Commands list
    "close", "exit", "." --> Exit from AddressBook
    
    *********** Add/edit command **********
    "add" name phone         --> Add user to AddressBook (for exampe +380.......)
    "change" name old_phone new_phone --> Change the user's phone number (for exampe +380.......)
    "birthday" name birthday --> Add/edit user birthday(dd.mm.yyyy)
    "email" name email       --> Add/edit user email
    "address" name address   --> Add/edit user address
    
    *********** Delete command ***********
    "del" name phone --> Delete phone number
    "delete" name    --> Delete user
    "clear"          --> Delete all users
    
    *********** Info command *************
    "show" name      --> Show user info
    "show all"       --> Show all users info
    "find" sub       --> Show all users info  with sub in name, phones or birthday
    "days to birthday" name --> Show how many days to user birthday
    "users birthday N" --> Show users with birthday in N days
    """


def unknown_command(*args):
    return 'Unknown command! Enter again!'


file_name = 'AddressBook.bin'


def writing_db(ab):
    with open(file_name, "wb") as fh:
        pickle.dump(ab, fh)


def reading_db():
    try:
        with open(file_name, "rb") as fh:
            unpacked = pickle.load(fh)
            return unpacked
    except (EOFError, FileNotFoundError):
        unpacked = AddressBook()
        return unpacked


COMMANDS = {greeting: ['hello'],
            add_contact: ['add '],
            change_contact: ['change '],
            info: ['help', '?'],
            show_all: ['show all'],
            exiting: ['good bye', 'close', 'exit', '.'],
            del_phone: ['del '],
            add_birthday: ['birthday'],
            days_to_user_birthday: ['days to birthday '],
            show_birthday_30_days: ['users birthday'],
            show_phone: ['show '],
            find: ['find'],
            del_user: ['delete '],
            clear_all: ['clear'],
            add_email: ['email '],
            add_address: ['address']}


def command_parser(user_command: str) -> (str, list):
    for key, list_value in COMMANDS.items():
        for value in list_value:
            if user_command.lower().startswith(value):
                args = user_command[len(value):].split()
                return key, args
    else:
        return unknown_command, []


def main():
    contacts = reading_db()
    print(info())
    while True:
        user_command = input('Enter command:>>> ')
        if user_command == 'exit':
            return f'Exit'
        command, data = command_parser(user_command)
        print(command(contacts, *data))
        if command is exiting:
            break
