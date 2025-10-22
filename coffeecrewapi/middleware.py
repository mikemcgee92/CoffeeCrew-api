from functools import wraps
from django.http import HttpResponse

def cors_allow_all(view_func):
    @wraps(view_func)
    def wrapped_view(*args, **kwargs):
        if args and hasattr(args[0], 'method'):
            request = args[0]
            if request.method == 'OPTIONS':
                response = HttpResponse()
                response['Content-Length'] = '0'
                response.status_code = 204  # No Content
            else:
                response = view_func(*args, **kwargs)

            # Always add CORS headers
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, PATCH, DELETE, OPTIONS'
            response['Access-Control-Allow-Headers'] = '*'  # Allow all headers
            response['Access-Control-Allow-Credentials'] = 'true'
            response['Access-Control-Max-Age'] = '86400'  # 24 hours
            
            # Add Vary header to prevent caching issues
            response['Vary'] = 'Origin'
            
            return response
        return view_func(*args, **kwargs)
    return wrapped_view
