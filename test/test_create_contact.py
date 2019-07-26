from random_word import RandomWords
from model.contacts import Contacts
from random import randint


def test_create_contact(app):
    r = RandomWords()
    phone = "+38093" + str(randint(0, 9999999))

    words_list = r.get_random_words()
    value = []
    for w in words_list:
        value.append(str(w))

    mail_list = r.get_random_words()
    mails = []
    for mail in mail_list:
        mails.append(str(mail) + "@mailer.com")
    contact = Contacts(first_name=value[1], last_name=value[2], mobile=phone, mail_1=mails[1],
                       mail_2=mails[2], mail_3=mails[3])
    app.contact.create(contact)
