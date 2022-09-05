from time import strptime

from src.db import session
from src.models import Contact, Phone


def create_contact(name, phone):
    contact = Contact(
        name=str(name))
    session.add(contact)
    session.commit()
    cont_id = session.query(Contact.id).filter(Contact.name == str(name)).scalar()
    phones = Phone(
        phone=str(phone),
        contacts_id=cont_id)
    session.add(phones)
    session.commit()


def update_contact(name, phone):
    cont_id = session.query(Contact.id).filter(Contact.name == str(name)).scalar()
    phones = Phone(
        phone=str(phone),
        contacts_id=cont_id)
    session.add(phones)
    session.commit()


def change_phone_db(name, old_phone, new_phone):
    data = session.query(Phone.id, Contact.id).join(Contact). \
        filter(Phone.phone == old_phone).filter(Contact.name == name).one()
    edit = session.query(Phone).get(data[0])
    edit.phone = new_phone
    edit.contacts_id = data[1]
    session.commit()


def update_email(name, email):
    id_ = session.query(Contact.id).filter(Contact.name == name).first()
    add = session.query(Contact).get(id_)
    add.email = email
    session.commit()


def update_address(name, address):
    id_ = session.query(Contact.id).filter(Contact.name == name).first()
    add = session.query(Contact).get(id_)
    add.address = address
    session.commit()


def update_birthday(name, birthday: str):
    id_ = session.query(Contact.id).filter(Contact.name == name).first()
    add = session.query(Contact).get(id_)
    temp = birthday.split('.')
    temp.reverse()
    birthday_db = '-'.join(temp)
    add.birthday = birthday_db
    session.commit()


def delete_phone(name, phone):
    data = session.query(Phone.id, Contact.id).join(Contact). \
        filter(Phone.phone == phone).filter(Contact.name == name).one()
    session.query(Phone).get(data[0]).delete()
    session.commit()


def delete_contact(name):
    session.query(Contact).filter(Contact.name == name).delete()
    session.commit()


def delete_all():
    session.query(Contact).delete()
    session.commit()
