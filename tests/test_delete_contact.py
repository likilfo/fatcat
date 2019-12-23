import random
from model.user import User

def test_delete_some_contact(app, create_contact, db, check_ui):
    old_contacts = create_contact
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    app.contact.wait_for\
        ('//*[contains(text(),"Delete record")]')
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=User.id_or_max) \
           == sorted(new_contacts, key=User.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=User.id_or_max) \
               == sorted(app.contact.get_contact_list(),
                         key=User.id_or_max)
