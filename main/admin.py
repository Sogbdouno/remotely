from django.contrib import admin
from main.models import Job
# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Job,JobAdmin)
