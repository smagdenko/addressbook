from model.contacts import Contacts

class ContactsHelper:

    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//*[@id='nav']//a[contains(text(),'add new')]").click()

    def create(self, contact):
        driver = self.app.driver
        self.open_contacts_page()
        self.fill_contact_fields(contact)

    def fill_contact_fields(self, contacts):
        driver = self.app.driver
        self.change_field_text("firstname", contacts.first_name)
        self.change_field_text("lastname", contacts.last_name)
        self.change_field_text("mobile", contacts.mobile)
        driver.find_element_by_xpath('.//*[@name="notes"]/following-sibling::input').click()


    def change_field_text(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def get_groups_list(self):
        driver = self.app.driver
        self.open_contacts_page()
        contacts = []
        for element in driver.find_elements_by_xpath("//*[@id='content']//span"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contacts(name=text, id=id))
        return contacts