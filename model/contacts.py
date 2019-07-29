class Contacts:

    def __init__(self, first_name=None, last_name=None, mobile=None, id=None, email_1=None, email_2=None, email_3=None):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.id = id
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3

    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) \
               and self.first_name == other.first_name and self.last_name==other.last_name