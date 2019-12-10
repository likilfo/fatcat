from .common import CommonHelper
from model.user import User
from time import sleep
import re


class ContactHelper(CommonHelper):

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

    contact_list_caсhe = None

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
        self.contact_list_caсhe = None

    def delete_contact_by_index(self, index):
        wd = self.wd
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath('//*[@value="Delete"]').click()
        alert = wd.switch_to.alert
        alert.accept()
        self.contact_list_caсhe = None

    def edit_first_contact(self, user, index):
        self.edit_contact_by_index(user, index)

    def edit_contact_by_index(self, user, index):
        wd = self.wd
        wd.find_element_by_link_text('home')
        wd.find_elements_by_xpath('//*[@title="Edit"]')[index].click()
        self.fill_contact_form(user, "update")
        self.contact_list_caсhe = None

    def delete_first(self, index):
        self.delete_contact_by_index(index)

    def get_contact_list(self):
        if self.contact_list_caсhe == None:
            wd = self.wd
            wd.find_element_by_link_text('home').click()
            sleep(2)
            self.contact_list_caсhe = []
            for element in wd.find_elements_by_name('entry'):
                name = element.find_element_by_xpath('.//td[3]').get_attribute("innerHTML")
                sername = element.find_element_by_xpath('.//td[2]').get_attribute("innerHTML")
                id = element.find_element_by_name('selected[]').get_attribute("value")
                sells = element.find_elements_by_tag_name('td')
                address = sells[3].text
                email = sells[4].text
                all_phones = sells[5].text
                self.contact_list_caсhe.append(User(firstname=name, lastname=sername, id=id,
                                                    address=address, all_phones=all_phones,
                                                    all_emails=email))
        return list(self.contact_list_caсhe)

    def clear(self, sring):
        return re.sub('[() -]', '', sring)

    def contacts_like_on_home_page(self, contacts):
        return '\n'.join(
            filter(lambda x: x != '', (
                map(lambda x: self.clear(x),
                    filter(lambda x: x is not None, contacts)))))

    def get_contact_from_edit_page(self, index):
        wd = self.wd
        wd.find_element_by_link_text('home').click()
        wd.find_elements_by_xpath('//*[@title="Edit"]')[index].click()
        name = wd.find_element_by_name('firstname').get_attribute("value")
        sername =wd.find_element_by_name('lastname').get_attribute("value")
        address = wd.find_element_by_name('address').get_attribute("value")
        home = wd.find_element_by_name('home').get_attribute("value")
        mobile = wd.find_element_by_name('mobile').get_attribute("value")
        work = wd.find_element_by_name('work').get_attribute("value")
        email = wd.find_element_by_name('email').get_attribute("value")
        email2 = wd.find_element_by_name('email2').get_attribute("value")
        email3 = wd.find_element_by_name('email3').get_attribute("value")
        all_phones = self.contacts_like_on_home_page([home, mobile, work])
        all_emails = self.contacts_like_on_home_page([email, email2, email3])
        return User(firstname=name, lastname=sername,
                     address=address, home=home, mobile=mobile,
                     work=work, email=email, email2=email2,
                     email3=email3, all_phones=all_phones,
                     all_emails=all_emails)
