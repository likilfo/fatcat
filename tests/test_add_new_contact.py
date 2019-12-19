from model.user import User


def test_add_new_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contact = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert len(old_contacts) == len(new_contact)
    assert sorted(old_contacts, key=User.id_or_max) \
           == sorted(new_contact, key=User.id_or_max)
