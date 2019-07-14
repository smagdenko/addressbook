class GroupSession:

    def __init__(self, app):
        self.app=app

    def create(self, group):

        driver = self.app.driver
        driver.find_element_by_xpath(".//*[@id='nav']/ul/li[3]/a").click()
        driver.find_element_by_xpath(".//*[@id='content']/form/input[1]").click()
        # New group
        self.fill_group_name(group)

    def fill_group_name(self, group):
        driver = self.app.driver
        self.change_field_text("group_name", group.name)
        self.change_field_text("group_header", group.header)
        self.change_field_text("group_footer", group.footer)
        driver.find_element_by_xpath(".//*[@type=\"submit\"]").click()

    def change_field_text(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def open_group_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("/groups") and len(driver.find_elements_by_xpath(".//*[@ name=\"new\"]"))>0):
            driver.find_element_by_xpath("//*[@id='nav']//a[contains(text(),'groups')]").click()

    def delete(self):
        driver = self.app.driver
        self.open_group_page()
        groups=driver.find_elements_by_xpath("//*[@id='content']//span")

        for _ in range(len(groups)):
            driver.find_element_by_xpath("//*[@id='content']//span[1]").click()
            driver.find_element_by_xpath("//input[2][@name='delete']").click()
            driver.find_element_by_xpath(".//*[@id='content']//a[contains(.,'group page')]").click()

    def modify_first_group(self, new_group_data):
        driver = self.app.driver
        driver.find_element_by_xpath("//*[@id='nav']//a[contains(.,'groups')]").click()
        driver.find_element_by_xpath(".//*[@id='content']/form/span[1]").click()
        driver.find_element_by_xpath("//input[3][@name='edit']").click()
        self.fill_group_name(new_group_data)
        driver.find_element_by_xpath(".//*[@id='content']//a[contains(.,'group page')]").click()

    def count(self):
        driver = self.app.driver
        self.open_group_page()
        return len(driver.find_elements_by_xpath("//*[@name=\"selected[]\"]"))