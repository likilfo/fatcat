from .common import CommonHelper
from model.user import User


class ContactHelper(CommonHelper):

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

    def fill_contact_form(self, user, submit):
        wd = self.wd
        self.fill_fields(user)
        wd.find_element_by_name(submit).click()
        wd.find_element_by_link_text("home").click()

    def is_exist(self):
        return len(self.wd.find_elements_by_name("selected[]"))

    def create(self, user):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(user, 'submit')

    def edit_first_contact(self, user):
        wd = self.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath('//*[@title="Edit"]').click()
        self.fill_contact_form(user, "update")

    def delete_first(self):
        wd = self.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath('//*[@value="Delete"]').click()
        alert = wd.switch_to.alert
        alert.accept()

    def get_contact_list(self):
        wd = self.wd
        contacts = []
        for element in wd.find_elements_by_name('entry'):
            name = element.find_element_by_xpath('.//td[3]').get_attribute("innerHTML")
            sername = element.find_element_by_xpath('.//td[2]').get_attribute("innerHTML")
            id = element.find_element_by_name('selected[]').get_attribute("value")
            contacts.append(User(firstname=name, lastname=sername, id=id))
        return contacts
