from model.group import Group


def test_modify_group(app):
    app.login(user="admin", password="secret")
    app.group.modify_first_group(Group(name="New group"))
    app.logout()
