# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group(app):
    app.login_by_admin()
    app.group.edit_first_group(Group(name='fitcat'))
    app.session.logout()