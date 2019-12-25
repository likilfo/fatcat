# -*- coding: utf-8 -*-
from model.group import Group
import allure


def test_add_some_group(app, db, json_groups, check_ui):
    with allure.step('Given a group list'):
        group = json_groups
        old_groups = db.get_group_list()
    with allure.allure.step('Create a group'):
        app.group.create(group)
    with allure.allure.step('Compare old and new group lists'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) \
               == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) \
                   == sorted(app.group.get_group_list(),
                             key=Group.id_or_max)




