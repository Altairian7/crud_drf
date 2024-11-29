from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def contact(request):
    return HttpResponse("To Contact us enter your mail: ")

def about(request):
    text = request.GET.get('text', 'default')
    print(text)
    return HttpResponse("We are what we are!")

def goback(request):
    return HttpResponse('<a href="/"> Go back to home </a>')