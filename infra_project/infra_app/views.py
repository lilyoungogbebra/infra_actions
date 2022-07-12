from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('У меня получилось!')


def second_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        if username:
            return HttpResponse(f'hello {username}')
        else:
            return HttpResponse('please, enter your username')
    return render(request, 'second_page.html')
