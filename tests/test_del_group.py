# -*- coding: utf-8 -*-
from model.group import Group


def test_del_group(app, create_group):
    old_groups = create_group
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == app.group.count()
    old_groups[0:1] = []
    assert old_groups == new_groups