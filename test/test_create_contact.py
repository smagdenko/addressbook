from random_words import RandomWords
from model.contacts import Contacts
from random import randint


def test_create_contact(app):
    r = RandomWords()

    phones=[]
    for _ in range(0,3):
        ph = "+38093" + str(randint(0, 9999999))
        phones.append(ph)

    words_list = r.random_words(count=5)
    value = []
    for w in words_list:
        value.append(str(w))

    mail_list = r.random_words(count=5)
    mails = []
    for mail in mail_list:
        mails.append(str(mail) + "@mailer.com")
    contact = Contacts(first_name=value[1], last_name=value[2], mobile_phone=phones[0],
                       home_phone=phones[1], work_phone=phones[2], email_1=mails[1])
    app.contact.create(contact)
