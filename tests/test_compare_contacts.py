from random import randrange
from model.user import User
import allure


def test_compare_comtact_from_home_and_edit_page(app, create_contact):
    with allure.step('Get contact from home page'):
        contacts = app.contact.get_contact_list()
        index = randrange(len(contacts))
        contact_from_home_page = contacts[index]
    with allure.step('Get contact from edit page'):
        contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    with allure.step('Compare contact from home and edit pages'):
        assert contact_from_home_page.firstname == contact_from_edit_page.firstname
        assert contact_from_home_page.lastname == contact_from_edit_page.lastname
        assert contact_from_home_page.address == contact_from_edit_page.address
        assert contact_from_home_page.all_phones == contact_from_edit_page.all_phones
        assert contact_from_home_page.all_emails == contact_from_edit_page.all_emails

def test_compare_comtact_from_home_and_bd(app, create_contact, db):
    with allure.step('Get contacts from home page'):
        contacts_from_ui = app.contact.get_contact_list()
    with allure.step('Get contacts from db'):
        contacts_from_bd = db.get_contact_list()
    with allure.step('Compare contacts from home page and db'):
        assert len(contacts_from_ui) == len(contacts_from_bd)
        sorted_ui = sorted(contacts_from_ui, key=User.id_or_max)
        sorted_bd = sorted(contacts_from_bd, key=User.id_or_max)
        for i in range(len(contacts_from_ui)):
            assert sorted_ui[i].firstname == sorted_bd[i].firstname
            assert sorted_ui[i].lastname == sorted_bd[i].lastname
            assert sorted_ui[i].address == sorted_bd[i].address
            assert sorted_ui[i].all_phones == sorted_bd[i].all_phones
            assert sorted_ui[i].all_emails == sorted_bd[i].all_emails
