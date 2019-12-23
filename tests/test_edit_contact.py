from model.user import User
import random


def test_edit_some_contact(app, create_contact, check_ui):
    old_contacts = create_contact
    contact = User(firstname='fitty')
    contact_id = random.choice(old_contacts)
    app.contact.edit_contact_by_id(contact, contact_id.id)
    contact.id = contact_id.id
    contact.lastname = contact_id.lastname
    new_contacts = app.contact.get_contact_list()
    index = old_contacts.index(contact_id)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=User.id_or_max) \
           == sorted(new_contacts, key=User.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=User.id_or_max) \
               == sorted(app.contact.get_contact_list(),
                         key=User.id_or_max)



