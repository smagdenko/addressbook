from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="new", header="bbbbbbbbbbb", footer="vcmvncmvn"))
    # app.group.delete()
    app.logout()


