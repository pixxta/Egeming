from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    return HttpResponse("Тестовая страница")

def home_page(request):
    return HttpResponse("Начальная страница")

def react_page(request):
    return render(request, 'react_page.html')
