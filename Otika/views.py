from django.shortcuts import render
from .models import *


def index(request):
    otika_bilgiler = InfoOtika.objects.all()
    context = {
        'otika_bilgiler': otika_bilgiler
    }
    return render(request, 'Home/index.html', context)