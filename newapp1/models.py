from django.db import models
class Todo(models.Model):
    title= models.CharField('Title_Name ',max_length=100)
    about=models.TextField('About_Title ')
    a=models.DateTimeField(auto_now_add=True)
    b=models.DateTimeField(auto_now=True)
    
