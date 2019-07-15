from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_groups_list()
    app.group.create(Group(name="new", header="bbbbbbbbbbb", footer="vcmvncmvn"))
    new_groups = app.group.get_groups_list()
    assert len(old_groups)+1 == len(new_groups)


