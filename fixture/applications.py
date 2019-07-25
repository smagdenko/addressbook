from fixture.group_page import GroupSession
from fixture.contacts_page import ContactsHelper


class Applications:

    def __init__(self, driver):
        self.driver=driver
        # self.driver.implicitly_wait(5)
        self.group = GroupSession(self)
        self.contact = ContactsHelper(self)

    def open_homepage(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def login(self, user, password):
        driver = self.driver
        self.open_homepage()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(user)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()

    def is_loged_in(self):
        driver = self.driver
        return len(driver.find_elements_by_link_text("Logout"))>0

    def is_loged_as(self, user):
        driver = self.driver
        return driver.find_element_by_xpath(".//*[@id='top']//b").text == ("("+ user +")")

    def ensure_login(self, user, password):
        driver = self.driver
        if self.is_loged_in():
            if self.is_loged_as(user):
                return
            else:
                self.logout()
        self.login(user, password)

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        driver = self.driver
        if len(driver.find_elements_by_link_text("Logout"))>0:
            self.logout()

    def destroy(self):
        self.driver.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
