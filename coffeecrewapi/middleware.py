from functools import wraps
from django.http import HttpResponse

def cors_allow_all(view_func):
    @wraps(view_func)
    def wrapped_view(*args, **kwargs):
        if args and hasattr(args[0], 'method') and args[0].method == 'OPTIONS':
            response = HttpResponse()
            response['Content-Length'] = '0'
            response.status_code = 200
        else:
            response = view_func(*args, **kwargs)

        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, PATCH, DELETE, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With'
        response['Access-Control-Max-Age'] = '86400'
        return response
    return wrapped_view
