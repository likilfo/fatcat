# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_del_some_group(app, db, create_group, check_ui):
    old_groups = create_group
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) \
               == sorted(app.group.get_group_list(),
                         key=Group.id_or_max)
