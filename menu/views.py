from django.shortcuts import render
from .models import Rubric

# создаём многоуровневое меню https://www.youtube.com/watch?v=DIS6e_oZOQA&list=PLmC7X4gkQWCeYJeFQID3m1f5I6SZgH9Vv&index=18&t=181s
def testmenu(request):
    return render(request, 'menu/testmenu.html', {'rubrics': Rubric.objects.all()})

def get_rubric(request):
    pass
