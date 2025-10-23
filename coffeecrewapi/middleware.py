from django.http import HttpResponse

def add_cors_headers(response, allowed_origin):
    response['Access-Control-Allow-Origin'] = allowed_origin
    response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

def handle_preflight(request):
    if request.method == 'OPTIONS':
        response = HttpResponse()
        return add_cors_headers(response, 'https://coffee-crew-api-git-deployment-mikes-projects-1f8906d9.vercel.app/')
