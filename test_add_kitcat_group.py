# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from entities import Group, User

class TestAddNewEntities(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox(
            executable_path=r'C:\Windows\SysWOW64\geckodriver.exe')
        self.wd.implicitly_wait(30)

    def open_home_page(self):
        self.base_url = "https://www.katalon.com/"

    def login(self, wd, login, password):
        wd.get("http://127.0.0.1/addressbook/")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()

    def login_by_admin(self, wd):
        self.login(wd, login='admin', password='secret')

    def open_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()


    def create_new_group(self, wd, group):
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

    def open_adding_new_contacts_page(self, wd):
        wd.find_element_by_link_text("add new").click()


    def create_new_contact(self, wd, user):
        for key, value in user.__dict__.items():
            wd.find_element_by_name(key).click()
            wd.find_element_by_name(key).clear()
            wd.find_element_by_name(key).send_keys(value)
        wd.find_element_by_name("submit").click()


    def return_to_group_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def test_add_kitcat_group(self):
        wd = self.wd
        self.open_home_page()
        self.login_by_admin(wd)
        self.open_group_page(wd)
        self.create_new_group(wd, Group(name='kitcat',
                                        header='kitcat group header',
                                        footer='kitcat group footer'))
        self.return_to_group_page(wd)


    def test_add_new_contact(self):
        wd = self.wd
        self.open_home_page()
        self.login_by_admin(wd)
        self.open_adding_new_contacts_page(wd)
        self.create_new_contact(wd, User(firstname='kitty',
                                         middlename='little',
                                         lastname='hwllo',
                                         nickname='likilfo',
                                         title='molly',
                                         company='Kit&Co'))


    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
