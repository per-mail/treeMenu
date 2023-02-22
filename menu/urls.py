from django.urls import path
from .views import *


# создаём древовидное меню
urlpatterns = [
    path('', menu, name='menu'),
    path('rubric/<int:pk>', get_rubric, name='rubric'),
]

