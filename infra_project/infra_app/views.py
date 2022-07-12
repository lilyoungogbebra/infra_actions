from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def second_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        if username:
            return HttpResponse('А это вторая страница')
        else:
            return HttpResponse('please, enter your username')
    return render(request, 'second_page.html')
