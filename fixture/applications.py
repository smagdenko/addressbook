from fixture.group import GroupSession

class Applications:

    def __init__(self, driver):
        self.driver=driver
        self.driver.implicitly_wait(5)
        self.group=GroupSession(self)

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

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.driver.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
