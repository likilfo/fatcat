from .common import CommonHelper
from model.group import Group
class GroupHelper(CommonHelper):

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

    group_cache_list = None

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
        self.group_cache_list = None

    def edit_first_group(self, index):
        self.delete_group_by_index(index)

    def edit_group_by_id(self, group, id):
        wd = self.wd
        self.select_group_by_id(id)
        wd.find_element_by_name("edit").click()
        self.fill_fields(group)
        wd.find_element_by_name("update").click()
        self.group_cache_list = None

    def get_group_list(self):
        if not self.group_cache_list:
            wd = self.wd
            self.open_group_page()
            self.group_cache_list = []
            for element in wd.find_elements_by_css_selector('span.group'):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache_list.append(Group(name=text, id=id))
        return self.group_cache_list

    def select_group_by_index(self, index):
        wd = self.wd
        self.open_group_page()
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.wd
        self.open_group_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()


    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_id(self, index):
        wd = self.wd
        self.select_group_by_id(index)
        wd.find_element_by_name("delete").click()
        wd.find_element_by_link_text("home").click()
        self.group_cache_list = None

    def count(self):
        wd = self.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))



