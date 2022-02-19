import re
from django.shortcuts import render

def index(request):
    return(request, 'home/index.html')
 