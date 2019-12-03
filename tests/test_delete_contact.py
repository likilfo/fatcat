

def test_delete_first_contact(app, create_contact):
    old_contacts = create_contact
    app.contact.delete_first()
    app.contact.wait_for\
        ('//*[contains(text(),"Delete record")]')
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts