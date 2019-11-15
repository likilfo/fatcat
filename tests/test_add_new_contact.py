from helpers import User

def test_add_new_contact(app):
    app.login_by_admin()
    app.create_new_contact(User(firstname='kitty',
                                     middlename='little',
                                     lastname='hwllo',
                                     nickname='likilfo',
                                     title='molly',
                                     company='Kit&Co'))
