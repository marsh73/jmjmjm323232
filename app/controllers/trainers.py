from ferris import Controller, scaffold, messages


class Trainers(Controller):
    class Meta:
        prefixes = ('admin','api')
        components = (scaffold.Scaffolding, messages.Messaging)

    admin_list = scaffold.list        #lists all posts
    admin_view = scaffold.view        #view a post
    admin_add = scaffold.add          #add a new post
    admin_edit = scaffold.edit        #edit a post
    admin_delete = scaffold.delete    #delete a post

    api_list = scaffold.list
    api_view = scaffold.view
    api_add = scaffold.add
    api_edit = scaffold.edit
    api_delete = scaffold.delete

    list = scaffold.list
    edit = scaffold.edit
    add = scaffold.add