#https://www.youtube.com/watch?v=w1OpC2VA3Lk&list=PLmC7X4gkQWCeYJeFQID3m1f5I6SZgH9Vv&index=20
from django.contrib import admin
#from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from .models import Rubric, Article

#admin.site.register(Rubric, MPTTModelAdmin)
admin.site.register(
    Rubric,
    DraggableMPTTAdmin,# реализует возможность перетаскивания курсором рубрики
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)
admin.site.register(Article)
