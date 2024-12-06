from django.shortcuts import render

# 직접 입력한 import
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're the polls index.")