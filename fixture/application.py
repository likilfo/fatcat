from selenium import webdriver
from .session import SessionHelper
from .group import GroupHelper
from .contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox(
            executable_path=r'C:\Windows\SysWOW64\geckodriver.exe')
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://127.0.0.1/addressbook/")

    def login_by_admin(self):
        self.session.login(login='admin', password='secret')

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()