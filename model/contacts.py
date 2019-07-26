class Contacts:

    def __init__(self, first_name=None, last_name=None, mobile=None, id=None, mails=None): #, mail_1=None, mail_2=None, mail_3=None):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.id = id
        self.mail_1 = mails[1]
        self.mail_2 = mails[2]
        self.mail_3 = mails[3]

    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) \
               and self.first_name == other.first_name and self.last_name==other.last_name