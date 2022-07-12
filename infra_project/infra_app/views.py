from django.http import HttpResponse


def index(request):
    html = 'У меня получилось!'
    return HttpResponse(html)


def second_page(request):
    html = 'А это вторая страница'
    return HttpResponse(html)
