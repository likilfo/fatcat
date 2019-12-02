from model.user import User

def test_delete_first_contact(app):
    app.contact.delete_first()