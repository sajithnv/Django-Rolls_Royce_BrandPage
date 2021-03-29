from django.contrib import admin
from newapp1.models import Todo
class display(admin.ModelAdmin):
	list_display=['title','about']
admin.site.register(Todo,display)
# Register your models here.
