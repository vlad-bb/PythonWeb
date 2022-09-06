import random
from faker import Factory
from src.db import session
from models import Contact, Phone
from time import time

fake = Factory.create('uk_UA')


def create_contacts(count):
    timer = time()
    for _ in range(count):
        contact = Contact(
            name=fake.first_name(),
            last_name=fake.last_name(),
            birthday=fake.date_between(start_date='-40y'),
            email=fake.email(),
            address=fake.address())
        session.add(contact)
    session.commit()
    create_phones()
    print(f'AddressBook was update with {count} new contacts during {round(time() - timer, 4)} sec')


def create_phones():
    contacts = session.query(Contact).all()
    for _ in range(len(list(contacts)) + 10):
        contact = random.choice(contacts)
        phones = Phone(phone=fake.phone_number(),
                       contacts_id=contact.id)
        session.add(phones)
    session.commit()


if __name__ == '__main__':
    create_contacts(50)

