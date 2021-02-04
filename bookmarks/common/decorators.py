from django.http import HttpResponseBadRequest


def ajax_required(f):
    def inner(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()
        return f(request, *args, **kwargs)
    inner.__doc__ = f.__doc__
    inner.__name__ = f.__name__
    return inner
