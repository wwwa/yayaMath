from django.contrib import admin

# Register your models here.
from bookmall.models import BookMall, Tag


class BookMallAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content','add_time']


admin.site.register(BookMall, BookMallAdmin)
admin.site.register(Tag)
