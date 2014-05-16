from ferris import Controller, scaffold


class Posts(Controller):
    class Meta:
        prefixes = ('admin',)
        components = (scaffold.Scaffolding,)

    admin_list = scaffold.list        #lists all posts
    admin_view = scaffold.view        #view a post
    admin_add = scaffold.add          #add a new post
    admin_edit = scaffold.edit        #edit a post
    admin_delete = scaffold.delete    #delete a post

    # list = scaffold.lost
    def list(self):
        if 'mine' in self.request.params:
            self.context['posts'] = self.meta.Model.all_posts_by_user()
        else:
            self.context['posts'] = self.meta.Model.all_posts()

    add = scaffold.add
    
    def edit(self, key):
        post = self.util.decode_key(key).get()

        if post.created_by != self.user:
            return 403

        return scaffold.edit(self, key)