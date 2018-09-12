from django.shortcuts import render
from django.http import HttpResponse

def index(reqquest):
    return HttpResponse("Hello, world.  You're at the polls index")


