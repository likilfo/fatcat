# -*- coding: utf-8 -*-
from model.group import Group


def test_del_group(app):
    app.login_by_admin()
    app.group.delete_first_group()
    app.session.logout()