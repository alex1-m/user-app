from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello, World!(homepage)<h1>")

def user(request, id):
    return HttpResponse(f"<h1>Hello, user <span style='color: red;'>{id}<span><h1>")