from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello world, You're at the news index")


def index123(request):
    return HttpResponse("Hello world, You're at the news index123")


def category(request):
    return render(request, 'pages/category.html', {})