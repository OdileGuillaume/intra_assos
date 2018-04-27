from django.shortcuts import HttpResponseRedirect


class AuthRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        if not request.user.is_authenticated():
            return HttpResponseRedirect('login')

        # Code to be executed for each request/response after
        # the view is called.

        return response
