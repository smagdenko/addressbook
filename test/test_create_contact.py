from model.contacts import Contacts
from random_word import RandomWords
from random import randint


def test_create_contact(app):
    r = RandomWords()
    # digits = "+38093" + randint(7)
    word = r.get_random_word()
    contact = (Contacts(first_name=word, last_name=word, mobile=word))
    app.contacts.create(contact)
