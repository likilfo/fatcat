# -*- coding: utf-8 -*-
from model.group import Group


def test_add_kitcat_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name='kitcat',
                           header='kitcat group header',
                           footer='kitcat group footer')
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(new_groups) - 1 == len(old_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) \
           == sorted(new_groups, key=Group.id_or_max)




