from django.shortcuts import render


def testmenu(request):
    return render(request, 'menu/menu.html')

def get_rubric(request):
    pass
