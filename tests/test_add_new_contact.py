from model.user import User
from fixture.common import CommonHelper
import pytest

c = CommonHelper()
test_data = [User(firstname='', middlename='',
                  lastname='', nickname='',
                  title='', company='', home='',
                  mobile='', work='', address='',
                  email='', email2='',email3='')] + \
            [User(firstname=c.random_string(),
                  middlename=c.random_string(),
                  lastname=c.random_string(),
                  nickname=c.random_string(),
                  title=c.random_string(),
                  company=c.random_string(),
                  address=c.random_address(),
                  home=c.random_phone(),
                  work=c.random_phone(),
                  mobile=c.random_phone(),
                  email=c.random_email(),
                  email2=c.random_email(),
                  email3=c.random_email())
             for i in range(5)]


@pytest.mark.parametrize('contact', test_data,
                         ids=[repr(x) for x in test_data])
def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contact = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert len(old_contacts) == len(new_contact)
    assert sorted(old_contacts, key=User.id_or_max) \
           == sorted(new_contact, key=User.id_or_max)
