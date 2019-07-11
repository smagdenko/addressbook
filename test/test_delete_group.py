from model.group import Group


def test_add_group(app):
    app.login(user="admin", password="secret")
    app.group.delete()
    app.logout()