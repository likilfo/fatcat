from model.user import User

def test_edit_contact(app, create_contact):
    app.contact.edit_first_contact(User(firstname='fitty'))