# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_edit_group(app, create_group):
    old_groups = create_group
    group = Group(name='fitcat')
    index = randrange(len(old_groups))
    id = old_groups[index].id
    app.group.edit_groupt_by_index(group, index)
    group.id = id
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) \
           == sorted(new_groups, key=Group.id_or_max)
