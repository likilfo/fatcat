from model.user import User
from random import randrange

def test_edit_some_contact(app, create_contact):
    old_contacts = create_contact
    index = randrange(len(old_contacts))
    contact = User(firstname='fitty')
    app.contact.edit_contact_by_index(contact, index)
    contact.id = old_contacts[index].id
    contact.lastname = old_contacts[index].lastname
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=User.id_or_max) \
           == sorted(new_contacts, key=User.id_or_max)

