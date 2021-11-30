import os

from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from datetime import datetime
# Create your views here.
from django_test import settings


def index(request):
    now = datetime.now()
    return render(request, 'index.html', {'now': now})


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def table(request):
    file_name = os.path.join(settings.BASE_DIR, "media/table/test.xlsx")
    f = open(file_name, 'rb')
    return FileResponse(f, content_type='application/vnd.ms-excel')