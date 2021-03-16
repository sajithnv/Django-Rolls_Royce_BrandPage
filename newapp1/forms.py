from django import forms
from newapp1.models import Todo
class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields={'about','title'}
