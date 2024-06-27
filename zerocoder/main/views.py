from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Это мой первый проект на Django</h2>")

def new(request):
    return HttpResponse("<h2>Это вторая страница моего проекта на Django</h2>")
