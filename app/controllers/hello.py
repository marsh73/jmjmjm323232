from ferris import Controller, route


class Hello(Controller):

    def list(self):
        # return "Hello, is it me you're looking for?"
        # return "Hello, %s" % self.request.params['name']
        self.context['who'] = self.request.params['name']

# @route
# def custom(self, text, person):
#     return "%s, %s, indeed." % (text, person)