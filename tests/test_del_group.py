# -*- coding: utf-8 -*-
from model.group import Group


def test_del_group(app, create_group):
    app.group.delete_first_group()