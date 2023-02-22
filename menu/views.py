from django.shortcuts import render
from .models import Rubric

def testmenu(request):
    return render(request, 'menu/testmenu.html')

def get_rubric(request):
    pass
