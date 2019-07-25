from random import randrange

from model.group import Group
from fixture.group_page import GroupSession


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='create for deleting'))
    old_groups = app.group.get_groups_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_groups_list()
    assert len(old_groups)-1 == len(new_groups)
    old_groups[index:index+1] = []    # delete first element of old_group list
    assert old_groups == new_groups
