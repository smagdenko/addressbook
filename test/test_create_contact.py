from random_word import RandomWords
from model.contacts import Contacts
from random import randint


def test_create_contact(app):
    r = RandomWords()
    digits = "+38093" + str(randint(0, 9999999))
    word = r.get_random_word()
    mail = r.get_random_words()
    mails = []
    for i in mail:
        mails.append(str(i) + "@mailer.com")
    contact = Contacts(first_name=word, last_name=word, mobile=digits, mail_1=mails[1], mail_2=mails[2], mail_3=mails[3])
    app.contact.create(contact)
