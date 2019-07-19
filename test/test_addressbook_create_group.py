from model.group import Group
from random_word import RandomWords


def test_add_group(app):
    r = RandomWords()
    word = r.get_random_word()
    group = (Group(name=word, header=word, footer=word))
    old_groups = app.group.get_groups_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_add_groups(app):
    r = RandomWords()
    for _ in range(3):
        word = r.get_random_word()
        old_groups = app.group.get_groups_list()
        app.group.create(Group(name=word, header=word, footer=word))
        new_groups = app.group.get_groups_list()
        assert len(old_groups)+1 == len(new_groups)

