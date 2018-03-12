from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Look at this beautiful page</h1>')
