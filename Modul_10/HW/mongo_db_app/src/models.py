from mongoengine import *

connect(host='mongodb://localhost:27017/addressbook')


class Contact(Document):
    name = StringField(max_length=100, required=True)
    last_name = StringField(max_length=100)
    phone = StringField(max_length=20, required=True)
    email = EmailField()
    birthday = DateField()
    address = StringField(max_length=500)
    meta = {'indexes': [
        {'fields': ['$name', "$last_name", "$phone", "$email", "$birthday", "$address"],
         'default_language': 'english',
         'weights': {'name': 10, 'last_name': 9, 'phone': 8, 'email': 7, 'birthday': 6, 'address':5}
         }
    ]}


