from model.group import Group
from fixture.group import GroupSession

def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='create for deleting'))
    app.group.delete()