
from model.group import Group


# @pytest.fixture
# def app(request):
#     fixture = Applications()
#     # request.addfinalizer(fixture.destroy())
#     return fixture


def test_add_group(app):
    app.login(user="admin", password="secret")
    app.group.create(Group(name="qweer", header="zxccxcv", footer="vcmvncmvn"))
    # app.group.delete()
    app.logout()






