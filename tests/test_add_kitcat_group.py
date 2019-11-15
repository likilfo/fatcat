# -*- coding: utf-8 -*-
from helpers import Group


def test_add_kitcat_group(app):
    app.login_by_admin()
    app.create_new_group(Group(name='kitcat',
                                    header='kitcat group header',
                                    footer='kitcat group footer'))





