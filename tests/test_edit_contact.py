from model.user import User

def test_edit_contact(app):
    app.contact.edit_first_contact(User(firstname='fitty'))