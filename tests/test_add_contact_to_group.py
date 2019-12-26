import random
import allure
from model.user import User

def test_add_contact_to_group(app, create_contact, create_group, db):
    with allure.step('Given a group list'):
        all_contacts = create_contact
    with allure.step('Add contact to a group'):
        contact_without_group = db.contact_not_in_group(all_contacts)
        if not contact_without_group:
            contact_name = app.contact.random_string()
            app.contact.create(User(firstname=contact_name, lastname='test1'))
            for contact in db.get_contact_list():
                if contact.firstname == contact_name:
                    contact_without_group = contact
        all_groups = create_group
        random_group = random.choice(all_groups)
        app.contact.add_to_group(contact_without_group.id, random_group.id)
    with allure.step('Contact is in a group'):
        groups_ids = db.get_groups_for_contact(contact_without_group.id)
        assert int(random_group.id) in groups_ids

def test_remove_contact_from_group(app, create_contact, create_group, db):
    with allure.step('Given a group list'):
        all_contacts = create_contact
    with allure.step('Add contact to a group'):
        all_groups = create_group
        contact_in_group, group_id = db.contact_in_group()
        if not contact_in_group:
            contact_in_group = random.choice(all_contacts)
            group = random.choice(all_groups)
            app.contact.add_to_group(contact_in_group, group.id)
            group_id = int(group.id)
            assert group_id in db.get_groups_for_contact(contact_in_group)
    with allure.step('Remove contact from a group'):
        app.contact.remove_from_group(str(contact_in_group), str(group_id))
    with allure.step('Contact is not in a group'):
        groups_ids = db.get_groups_for_contact(contact_in_group)
        assert group_id not in groups_ids