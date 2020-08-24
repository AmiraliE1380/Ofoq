from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def articles_list(request):
    return HttpResponse("Temporary layout for the articles menu")