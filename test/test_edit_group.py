from model.group import Group


def test_edit_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="New group"))
    app.session.logout()


def test_edit_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="New header"))
    app.session.logout()









#def test_edit_first_group(app):
    #app.session.login(username="admin", password="secret")
    #app.group.edit_first_group()
    #app.session.logout()