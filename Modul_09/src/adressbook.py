import datetime
from datetime import date
import re
import phonenumbers
from abc import ABC, abstractmethod
from src.dml import *


class Field(ABC):
    def __init__(self, value: str) -> None:
        self.__value = None
        self.value = value

    def __repr__(self) -> str:
        return f'{self.value}'

    def __str__(self) -> str:
        return f'{self.value}'

    def __eq__(self, other) -> bool:
        return self.value == other.value

    @abstractmethod
    def value(self):
        ...


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
    def value(self, value):
        try:
            number = phonenumbers.parse(value, "ITU-T")
            self.__value = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164)
        except Exception:
            print("Enter correct number, for example +380987654321")
            raise ValueError


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
    def __init__(self, name: Name, phones=None, birthday=None, email=None, address=None) -> None:
        if phones is None:
            phones = []
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

    @staticmethod
    def days_to_birthday(self, birthday: Birthday):
        if birthday.value is None:
            return None
        this_day = date.today()
        birthday_day = date(this_day.year, birthday.value.month, birthday.value.day)
        if birthday_day < this_day:
            birthday_day = date(this_day.year + 1, birthday.value.month, birthday.value.day)
        return (birthday_day - this_day).days


class InputError:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args):
        try:
            return self.func(*args)
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
def add_contact(*args):
    name = Name(args[0])
    if len(args) == 3:
        last_name = args[1]
        phone = Phone(args[2])
    elif len(args) == 2:
        phone = Phone(args[1])
    if check_name(name):
        update_contact(name, phone)
        return f'Contact {name.value.title()} add phone: {phone}'
    else:
        create_contact(name, last_name, phone)
        return f'Add user {name.value.title()} with phone number {phone}'


@InputError
def change_contact(*args):
    name, old_phone, new_phone = args[0], args[1], args[2]
    change_phone_db(name, old_phone, new_phone)
    return f'Change to user {name} phone number from {old_phone} to {new_phone}'


@InputError
def show_phone(*args):
    name = args[0]
    return show_phone_db(name)


@InputError
def del_phone(*args):
    name, phone = args[0], args[1]
    delete_phone(name, phone)
    return f'Delete phone {phone} from user {name}'


@InputError
def show_all(*args):
    return show_all_db()


@InputError
def add_email(*args):
    name, email = args[0], args[1]
    update_email(name, email)
    return f'Add/modify email {email} to user {name}'


@InputError
def add_last_name(*args):
    name, last_name = args[0], args[1]
    update_last_name(name, last_name)
    return f'Add/modify last name {last_name} to user {name}'


@InputError
def add_address(*args):
    name, address = args[0], list(args[1:])
    address = " ".join(address)
    update_address(name, address)
    return f'Add/modify address {address.title()} to user {name}'


@InputError
def add_birthday(*args):
    name, birthday = args[0], args[1]
    update_birthday(name, args[1])
    return f'Add/modify birthday {birthday} to user {name}'


@InputError
def user_birthday(*args):
    name = args[0]
    birthday = show_birthday(name)
    if not birthday:
        return 'User has no birthday'
    else:
        return f'Birthday {name} in: {birthday}'


def exiting():
    return 'Good bye!'


@InputError
def del_user(*args):
    name = args[0]
    yes_no = input(f'Are you sure you want to delete the user {name}? (y/n) ')
    if yes_no == 'y':
        delete_contact(name)
        return f'Delete user {name}'

    else:
        return 'User not deleted'


@InputError
def clear_all():
    yes_no = input('Are you sure you want to delete all users? (y/n) ')
    if yes_no == 'y':
        delete_all()
        return 'Address book is empty'
    else:
        return 'Removal canceled'


@InputError
def find(*args):
    sub = ' '.join(args)
    data = find_data(sub)
    return data


def info():
    return """
    *********** Service command ***********
    "help", "?"          --> Commands list
    "close", "exit", "." --> Exit from AddressBook
    
    *********** Add/edit command **********
    "add" name phone                  --> Add user to AddressBook
    "change" name old_phone new_phone --> Change the user's phone number
    "birthday" name birthday          --> Add/edit user birthday
    "email" name email                --> Add/edit user email
    "last name" name last name        --> Add/edit user last name
    "address" name address            --> Add/edit user address
    
    *********** Delete command ***********
    "del" name phone --> Delete phone number
    "delete" name    --> Delete user
    "clear"          --> Delete all users
    
    *********** Info command *************
    "show" name          --> Show user info
    "show all"           --> Show all users info
    "user birthday" name --> Show how many days to user birthday
    "find" data          --> Find any data 
    """


def unknown_command(*args):
    return 'Unknown command! Enter again!'


COMMANDS = {greeting: ['hello'],
            add_contact: ['add '],
            change_contact: ['change '],
            info: ['help', '?'],
            show_all: ['show all'],
            exiting: ['good bye', 'close', 'exit', '.'],
            del_phone: ['del '],
            add_birthday: ['birthday'],
            user_birthday: ['user birthday '],
            show_phone: ['show '],
            del_user: ['delete '],
            clear_all: ['clear'],
            add_email: ['email '],
            add_address: ['address'],
            add_last_name: ['last name'],
            find: ['find']}


def command_parser(user_command: str) -> (str, list):
    for key, list_value in COMMANDS.items():
        for value in list_value:
            if user_command.lower().startswith(value):
                args = user_command[len(value):].split()
                return key, args
    else:
        return unknown_command, []


def main():
    print(info())
    while True:
        user_command = input('Enter command:>>> ')
        if user_command == 'exit':
            return f'Exit'
        command, data = command_parser(user_command)
        print(command(*data))
        if command is exiting:
            break
