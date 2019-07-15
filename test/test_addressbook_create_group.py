from model.group import Group
from random_word import RandomWords


def test_add_group(app):
    r = RandomWords()
    word = r.get_random_word()
    old_groups = app.group.get_groups_list()
    app.group.create(Group(name=word, header=word, footer=word))
    new_groups = app.group.get_groups_list()
    assert len(old_groups) + 1 == len(new_groups)

def test_add_groups(app):
    r = RandomWords()
    for _ in range(3):
        word = r.get_random_word()
        old_groups = app.group.get_groups_list()
        app.group.create(Group(name=word, header=word, footer=word))
        new_groups = app.group.get_groups_list()
        assert len(old_groups)+1 == len(new_groups)

