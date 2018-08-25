from django.shortcuts import render


class View(object):
    http = ['post', 'get']

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value) # self.key = value

    @classmethod
    def as_view(cls, **kwargs):
        self = cls(**kwargs)

        def wrapper(request, *args, **kwargs):
            self.request = request
            return self.dispatch(request, *args, **kwargs)

        return wrapper

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.http:
            handler = getattr(self, request.method.lower()) # self.get
        else:
            handler = getattr(self, "not_found")
        return handler(request, *args, **kwargs)


class TemplateView(View):
    template_name = None

    def get(self, request, *args, **kwargs):
        if self.template_name:
            return render(request, self.template_name, self.get_context_data(**kwargs))
        else:
            raise ValueError()

    def get_context_data(self, **kwargs):
        context = {
            'form':"asdad"
        }
        return context
