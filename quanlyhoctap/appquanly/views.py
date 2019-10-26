from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Xin chào các bạn đến với web quản lý.")

# Create your views here.
