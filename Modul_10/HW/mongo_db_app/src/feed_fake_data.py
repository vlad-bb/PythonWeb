from datetime import datetime
from time import time

from HW.mongo_db_app.src.models import Contact
from faker import Faker

# for Ukranian people
fake = Faker('uk_UA')

# for foreign people
# fake = Faker()


def create_contacts(count):
    timer = time()
    for _ in range(count):
        Contact(
            name=fake.first_name(),
            last_name=fake.last_name(),
            phone=sanitize_phone(fake.phone_number()),
            birthday=fake.date_between_dates(date_start=datetime(1970, 1, 1), date_end=datetime(2006, 12, 31)),
            email=fake.ascii_free_email(),
            address=fake.address()).save()

    print(f'AddressBook was update with {count} new contacts during {round(time() - timer, 4)} sec')


def sanitize_phone(phone):
    new_phone = (phone.strip()
                 .removeprefix('+')
                 .replace("(", '')
                 .replace(")", '')
                 .replace(" ", '')
                 .replace("-", '')
                 .replace(".", ''))

    return new_phone


if __name__ == '__main__':
    create_contacts(10)
