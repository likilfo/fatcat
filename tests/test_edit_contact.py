from model.user import User

def test_edit_contact(app, create_contact):
    old_contacts = create_contact
    contact = User(firstname='fitty')
    app.contact.edit_first_contact(contact)
    contact.id = old_contacts[0].id
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=User.id_or_max) \
           == sorted(new_contacts, key=User.id_or_max)

