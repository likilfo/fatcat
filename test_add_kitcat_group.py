# -*- coding: utf-8 -*-
from entities import Group, User
from application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_kitcat_group(app):
    app.login_by_admin()
    app.create_new_group(Group(name='kitcat',
                                    header='kitcat group header',
                                    footer='kitcat group footer'))


def test_add_new_contact(app):
    app.login_by_admin()
    app.create_new_contact(User(firstname='kitty',
                                     middlename='little',
                                     lastname='hwllo',
                                     nickname='likilfo',
                                     title='molly',
                                     company='Kit&Co'))



