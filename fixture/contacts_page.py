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
        self.change_field_text("mobile", contacts.mobile_phone)
        self.change_field_text("home", contacts.home_phone)
        self.change_field_text("work", contacts.work_phone)
        self.change_field_text("email", contacts.email_1)
        self.change_field_text("email2", contacts.email_2)
        self.change_field_text("email3", contacts.email_3)
        driver.find_element_by_xpath('.//*[@name="notes"]/following-sibling::input').click()

    def change_field_text(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def open_contact_to_edit_by_index(self, index):
        driver = self.app.driver
        # row = driver.find_elements_by_xpath(".//*[@id='maintable']//td[7]")[index]
        # cell = row.find_element_by_name("entry")
        # cell.find_element_by_tag_name('a').click()

        driver.find_element_by_xpath('//*[@name="entry"][%s]//td[8]//img' % index).click()

    def get_info_from_edit_page(self, index):
        driver = self.app.driver
        self.open_contact_to_edit_by_index(index)
        firstname = driver.find_element_by_name("firstname").get_attribute("value")
        lastname = driver.find_element_by_name("lastname").get_attribute("value")
        email_1 = driver.find_element_by_name("email").get_attribute("value")
        email_2 = driver.find_element_by_name("email2").get_attribute("value")
        email_3 = driver.find_element_by_name("email3").get_attribute("value")
        mobile = driver.find_element_by_name("mobile").get_attribute("value")
        home = driver.find_element_by_name("home").get_attribute("value")
        work = driver.find_element_by_name("work").get_attribute("value")
        return Contacts(first_name=firstname, last_name=lastname, email_1=email_1, email_2=email_2, email_3=email_3,
                        mobile_phone=mobile, home_phone=home, work_phone=work)

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            driver = self.app.driver
            # self.open_contacts_page()
            self.contact_cache = []
            for row in driver.find_elements_by_xpath('//*[@name="entry"]'):
                element = driver.find_elements_by_tag_name("td")
                firstname = element[3].text
                lastname = element[2].text
                id = element[1].find_element_by_xpath("//input[@name='selected[]']").get_attribute("value")
                all_mails = element[4].text.splitlines()
                all_phones = element[5].text.splitlines()
                self.contact_cache.append(Contacts(first_name=firstname, last_name=lastname, id=id,
                                                    email_1=all_mails[0], email_2=all_mails[1], email_3=all_mails[2],
                                                    work_phone=all_phones[2], home_phone=all_phones[0], mobile_phone=all_phones[1]))
        return list(self.contact_cache)

