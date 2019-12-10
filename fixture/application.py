from selenium import webdriver
from .session import SessionHelper
from .group import GroupHelper
from .contact import ContactHelper


class Application:

    def __init__(self, browser, url):
        if browser == 'firefox':
            self.wd = webdriver.Firefox(
                executable_path=r'C:\Windows\SysWOW64\geckodriver.exe')
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError('Unrecognized browser %s' % browser)
        self.url = url
        self.wd.implicitly_wait(2)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get(self.url)

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
