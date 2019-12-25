from model.user import User
import allure


def test_add_new_contact(app, json_contacts, db, check_ui):
    with allure.step('Given a contact list'):
        contact = json_contacts
        old_contacts = db.get_contact_list()
    with allure.step('Create new contact'):
        app.contact.create(contact)
    with allure.step('Compare old and new contact lists'):
        new_contacts = db.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=User.id_or_max) \
               == sorted(new_contacts, key=User.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=User.id_or_max) \
                   == sorted(app.contact.get_contact_list(),
                             key=User.id_or_max)
