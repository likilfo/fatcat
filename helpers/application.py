from selenium import webdriver


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox(
            executable_path=r'C:\Windows\SysWOW64\geckodriver.exe')
        self.wd.implicitly_wait(30)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://127.0.0.1/addressbook/")

    def login(self, login, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()

    def login_by_admin(self):
        self.login(login='admin', password='secret')

    def open_group_page(self):
        self.wd.find_element_by_link_text("groups").click()

    def create_new_group(self, group):
        wd = self.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()

    def create_new_contact(self, user):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()
        for key, value in user.__dict__.items():
            wd.find_element_by_name(key).click()
            wd.find_element_by_name(key).clear()
            wd.find_element_by_name(key).send_keys(value)
        wd.find_element_by_name("submit").click()

    def destroy(self):
        self.wd.quit()