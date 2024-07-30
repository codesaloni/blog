from django.contrib import admin
from .models import *

class cateroryAdmin(admin.ModelAdmin):
    list_display=('images_tag','title','description','url','add_date')
    search_fields=("title",)


class postAdmin(admin.ModelAdmin):
    list_display=('title',)
    search_fields=('title',)
    list_filter=('cat',)
    list_per_page=50
admin.site.register(caterory,cateroryAdmin,)

admin.site.register(post,postAdmin)
