from django.contrib import admin
from .models import Student, Language, Framework,Page
# Register your models here.

admin.site.register(Student)
admin.site.register(Language)
admin.site.register(Framework)

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['page_name','page_cat','page_publish_date','user']


# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['id','name', 'roll', 'city']
