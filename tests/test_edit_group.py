# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group(app, create_group):
    old_groups = create_group
    group = Group(name='fitcat')
    id = old_groups[0].id
    app.group.edit_first_group(group)
    group.id = id
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) \
           == sorted(new_groups, key=Group.id_or_max)
