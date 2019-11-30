from .common import CommonHelper

class GroupHelper(CommonHelper):

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

    def open_group_page(self):
        self.wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        self.fill_fields(group)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()
        wd.find_element_by_link_text("home").click()

    def edit_first_group(self, group):
        wd = self.wd
        self.open_group_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        self.fill_fields(group)
        wd.find_element_by_name("update").click()


    def delete_first_group(self):
        wd = self.wd
        self.open_group_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        wd.find_element_by_link_text("home").click()




