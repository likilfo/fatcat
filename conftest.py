import pytest
from model.group import Group
from model.user import User
from fixture.application import Application

fixture = None

@pytest.fixture
def app():
    global fixture
    if not fixture:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login('admin', 'secret')
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return app

@pytest.fixture
def create_group():
    if not fixture.group.is_exist():
        if fixture.group.count() == 0:
            fixture.group.create(Group(name='kitcat',
                               header='kitcat group header',
                               footer='kitcat group footer'))
    return fixture.group.get_group_list()


@pytest.fixture
def create_contact():
    if not fixture.contact.is_exist():
        fixture.contact.create(User(firstname='kitty',
                                     middlename='little',
                                     lastname='hwllo',
                                     nickname='likilfo',
                                     title='molly',
                                     company='Kit&Co'))
    return fixture.contact.get_contact_list()