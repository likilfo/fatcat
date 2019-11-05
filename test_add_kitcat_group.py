# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from group import Group

class TestAddKitcatGroup(unittest.TestCase):
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

    def return_to_group_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def test_add_kitcat_group(self):
        wd = self.wd
        self.open_home_page()
        self.login_by_admin(wd)
        self.open_home_page(wd)
        self.create_new_group(wd, Group(name='kitcat',
                                        header='kitcat group header',
                                        footer='kitcat group footer'))
        self.return_to_group_page(wd)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
