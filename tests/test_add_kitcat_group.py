# -*- coding: utf-8 -*-
from model.group import Group


def test_add_kitcat_group(app):
    app.group.create(Group(name='kitcat',
                           header='kitcat group header',
                           footer='kitcat group footer'))





