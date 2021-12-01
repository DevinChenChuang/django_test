import os

from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from datetime import datetime
# Create your views here.
from django.views.generic import TemplateView

from django_test import settings


def index(request):
    now = datetime.now()
    money2 = 1000000000.69
    return render(request, 'index.html', {'now': now, 'money2': money2})


# def login(request):
#     return render(request, 'login.html')


class Login(TemplateView):
    template_name = "login.html"


def register(request):
    return render(request, 'register.html')


def table(request):
    file_name = os.path.join(settings.BASE_DIR, "media/table/test.xlsx")
    f = open(file_name, 'rb')
    return FileResponse(f, content_type='application/vnd.ms-excel')