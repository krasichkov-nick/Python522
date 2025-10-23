from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    lst = list(range(6, 15))
    return render(request, "generator/home.html", {"lst": lst})


def password(request):
    char = [chr(i) for i in range(97, 123)]

    if request.GET.get('uppercase'):
        char.extend([chr(i) for i in range(65, 91)])

    if request.GET.get('numbers'):
        char.extend([chr(i) for i in range(48, 57)])

    if request.GET.get('special'):
        char.extend([chr(i) for i in range(33, 47)])

    print(char)

    length = int(request.GET.get('length'))
    psw = ""
    for i in range(length):
        psw += random.choice(char)
    return render(request, "generator/password.html", {'password': psw})


def desk(request):
    desk_title = 'Описание работы программы'
    desk_add_text = 'Добавляем/убираем использование'
    context = {'desk_title': desk_title, 'desk_add_text': desk_add_text}
    return render(request, "generator/desk.html", context)