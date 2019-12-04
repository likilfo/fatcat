from random import randrange

def test_delete_some_contact(app, create_contact):
    old_contacts = create_contact
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    app.contact.wait_for\
        ('//*[contains(text(),"Delete record")]')
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index-1] = []
    assert old_contacts == new_contacts