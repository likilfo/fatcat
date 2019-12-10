from random import randrange


def test_compare_comtact_from_home_and_edit_page(app, create_contact):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = contacts[index]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones == contact_from_edit_page.all_phones
    assert contact_from_home_page.all_emails == contact_from_edit_page.all_emails