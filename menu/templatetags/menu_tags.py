from django import template
from menu.models import Rubric

# регистрируем тэг
register = template.Library()

# тэг возвращает список рубрик
@register.simple_tag()
def get_rubrics():
    return  Rubric.objects.all()


