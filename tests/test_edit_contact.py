from model.user import User

def test_edit_contact(app):
    app.login_by_admin()
    app.contact.edit_first_contact(User(firstname='fitty'))
    app.session.logout()
