from model.group import Group
from fixture.group import GroupSession


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='create for deleting'))
    old_groups = app.group.get_groups_list()
    app.group.delete_first_group()
    new_groups = app.group.get_groups_list()
    assert len(old_groups)-1 == len(new_groups)
    old_groups[0:1] = []    # delete first element of old_group list
    assert old_groups == new_groups
