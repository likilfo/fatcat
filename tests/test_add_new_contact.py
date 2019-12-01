from model.user import User

def test_add_new_contact(app):
    app.contact.create(User(firstname='kitty',
                                     middlename='little',
                                     lastname='hwllo',
                                     nickname='likilfo',
                                     title='molly',
                                     company='Kit&Co'))
