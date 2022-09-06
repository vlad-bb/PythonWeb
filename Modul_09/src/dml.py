import sqlalchemy
from sqlalchemy.orm import joinedload
from src.db import session
from src.models import Contact, Phone


class ExceptError:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args):
        try:
            return self.func(*args)
        except sqlalchemy.exc.NoResultFound:
            print('Not found this command')
        except sqlalchemy.exc.MultipleResultsFound:
            print('This phone already exsist')


@ExceptError
def create_contact(name, last_name, phone):
    contact = Contact(
        name=str(name),
        last_name=last_name)
    session.add(contact)
    session.commit()
    cont_id = session.query(Contact.id).filter(Contact.name == str(name)).scalar()
    phones = Phone(
        phone=str(phone),
        contacts_id=cont_id)
    session.add(phones)
    session.commit()


@ExceptError
def update_contact(name, phone):
    cont_id = session.query(Contact.id).filter(Contact.name == str(name)).first()
    phones = Phone(
        phone=str(phone),
        contacts_id=cont_id[0])
    session.add(phones)
    session.commit()


@ExceptError
def change_phone_db(name, old_phone, new_phone):
    data = session.query(Phone.id, Contact.id).join(Contact). \
        filter(Phone.phone == old_phone).filter(Contact.name == name).scalar()
    edit = session.query(Phone).get(data)
    edit.phone = new_phone
    session.commit()


@ExceptError
def update_email(name, email):
    id_ = session.query(Contact.id).filter(Contact.name == name).first()
    add = session.query(Contact).get(id_)
    add.email = email
    session.commit()


@ExceptError
def update_last_name(name, last_name):
    id_ = session.query(Contact.id).filter(Contact.name == name).first()
    add = session.query(Contact).get(id_)
    add.last_name = last_name
    session.commit()


@ExceptError
def update_address(name, address):
    id_ = session.query(Contact.id).filter(Contact.name == name).first()
    add = session.query(Contact).get(id_)
    add.address = address
    session.commit()


@ExceptError
def update_birthday(name, birthday: str):
    id_ = session.query(Contact.id).filter(Contact.name == name).first()
    add = session.query(Contact).get(id_)
    temp = birthday.split('.')
    temp.reverse()
    birthday_db = '-'.join(temp)
    add.birthday = birthday_db
    session.commit()


@ExceptError
def delete_phone(name, phone):
    data = session.query(Phone.id, Contact.id).join(Contact). \
        filter(Phone.phone == phone).filter(Contact.name == name).one()
    session.query(Phone).get(data[0]).delete()
    session.commit()


@ExceptError
def delete_contact(name):
    session.query(Contact).filter(Contact.name == name).delete()
    session.commit()


@ExceptError
def delete_all():
    session.query(Contact).delete()
    session.commit()


@ExceptError
def check_name(name):
    contact = session.query(Contact).filter(Contact.name == str(name)).scalar()
    if not contact:
        return False
    else:
        return True


@ExceptError
def show_phone_db(name):
    phones = session.query(Phone.id).join(Contact).filter(Contact.name == name).all()
    if not phones:
        return f'Contact {name} not found'
    else:
        print(f'Contact {name} have: ', end=' ')
        for phone in phones:
            for i in phone:
                number = session.query(Phone).filter(Phone.id == i).one()
                print(f'{number.phone}', end=' ')
        return f''


@ExceptError
def show_all_db():
    results = session.query(Contact, Phone.phone).join(Phone).all()
    result = 'List of all users:\n'
    for user, phones in results:
        result += f'Contact {user.name} {user.last_name} has phone: {phones}, birthday: {user.birthday}, email: {user.email}, address: {user.address}\n'
    session.commit()
    return result


@ExceptError
def show_birthday(name):
    contact = session.query(Contact).filter(Contact.name == name).first()
    birthday = contact.birthday
    session.commit()
    return birthday


@ExceptError
def find_data(sub):
    results = session.query(Contact, Phone.phone).join(Phone).all()
    for user, phones in results:
        birthday = user.birthday.strftime("%Y-%m-%d")
        if sub in user.name or sub in user.last_name or sub in phones \
                or sub in birthday or sub in user.email or sub in user.address:
            return f'User {user.name} {user.last_name},' \
                   f' phone: {phones},' \
                   f' birthday: {user.birthday},' \
                   f' email: {user.email},' \
                   f' address: {user.address}'
        else:
            return f'Not data for your request {sub}'

