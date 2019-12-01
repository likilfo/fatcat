from .common import CommonHelper
from model.group import Group
class GroupHelper(CommonHelper):

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

    def open_group_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/group.php")
                and len(wd.find_elements_by_name('new')) > 0):
            self.wd.find_element_by_link_text("groups").click()

    def is_exist(self):
        self.open_group_page()
        return len(self.wd.find_elements_by_name("selected[]"))

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

    def get_group_list(self):
        wd = self.wd
        self.open_group_page()
        groups = []
        for element in wd.find_elements_by_css_selector('span.group'):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            groups.append(Group(name=text, id=id))
        return groups

    def delete_first_group(self):
        wd = self.wd
        self.open_group_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        wd.find_element_by_link_text("home").click()




