from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('У меня получилось!')


def second_page(request):
    if request.method == "POST":
        return HttpResponse('А это вторая страница')
    return render(request, 'second_page.html')
