
from model.group import Group


# @pytest.fixture
# def app(request):
#     fixture = Applications()
#     # request.addfinalizer(fixture.destroy())
#     return fixture


def test_add_group(app):
    app.group.create(Group(name="new", header="bbbbbbbbbbb", footer="vcmvncmvn"))
    # app.group.delete()
    app.logout()






