# myapp/forms.py
from django import forms
from .models import MyFileModel

class MyFileForm(forms.Form):
    file = forms.FileField()