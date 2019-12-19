# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from generator.groups import test_data

@pytest.mark.parametrize('group', test_data,
                         ids=[repr(x) for x in test_data])
def test_add_some_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert app.group.count() - 1 == len(old_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) \
           == sorted(new_groups, key=Group.id_or_max)




