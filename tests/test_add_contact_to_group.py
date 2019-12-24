import random

def test_add_contact_to_group(app, create_contact, create_group, db):
    all_contacts = create_contact
    random_contact = random.choice(all_contacts)
    all_groups = create_group
    random_group = random.choice(all_groups)
    app.contact.add_to_group(random_contact.id, random_group.id)
    groups_ids = db.get_groups_for_contact(random_contact.id)
    assert random_group.id in groups_ids

def test_remove_contact_from_group(app, create_contact, create_group, db):
    all_contacts = create_contact
    random_contact = random.choice(all_contacts)
    all_groups = create_group
    random_group = random.choice(all_groups)
    app.contact.add_to_group(random_contact.id, random_group.id)
    groups_ids = db.get_groups_for_contact(random_contact.id)
    assert random_group.id in groups_ids
    app.contact.remove_from_group(random_contact.id, random_group.id)
    groups_ids = db.get_groups_for_contact(random_contact.id)
    assert random_group.id not in groups_ids