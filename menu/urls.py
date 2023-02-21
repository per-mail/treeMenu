from django.urls import path
from .views import *
# создаём древовидное меню
urlpatterns = [
    path('', testmenu, name='testmenu'),
    path('rubric/<int:pk>', get_rubric, name='rubric'),    
]

