# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group(app, create_group):
    app.group.edit_first_group(Group(name='fitcat'))