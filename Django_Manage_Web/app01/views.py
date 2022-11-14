from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('欢迎来到Django的世界，Hello World！')