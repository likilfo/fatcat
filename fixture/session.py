from time import sleep

class SessionHelper:

    def __init__(self, app):
        self.app = app
        self.app.open_home_page()

    def login(self, login, password):
        wd = self.app.wd
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()


    def is_logged_in(self):
        return len(self.app.wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, user):
        return self.app.wd.find_element_by_xpath(
            "//div/div[1]/form/b").text == "("+user+")"

    def logout(self):
        for attemtp in range(2):
            try:
                self.app.wd.find_element_by_link_text("Logout").click()
            except:
                pass

    def ensure_logout(self):
        if len(self.app.wd.find_elements_by_link_text("Logout")) > 0:
            self.logout()

    def ensure_login(self, user, password):
        if self.is_logged_in():
            if not self.is_logged_in_as(user):
                self.logout()
                self.login(user, password)
        else:
            self.login(user, password)