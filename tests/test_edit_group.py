# -*- coding: utf-8 -*-
from model.group import Group
import random, allure


def test_edit_group(app, create_group, db, check_ui):
    with allure.step('Given a group list'):
        old_groups = create_group
    with allure.step('Edit a group'):
        group = Group(name='fitcat')
        group_id = random.choice(old_groups)
        app.group.edit_group_by_id(group, group_id.id)
    with allure.step('Compare old and new group lists'):
        new_groups = db.get_group_list()
        index = old_groups.index(group_id)
        old_groups[index] = group
        assert sorted(old_groups, key=Group.id_or_max) \
               == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) \
                   == sorted(app.group.get_group_list(),
                             key=Group.id_or_max)
