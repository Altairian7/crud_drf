from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> Hi Mom </h1>")

def contact(request):
    return HttpResponse("To Contact us enter your mail: ")