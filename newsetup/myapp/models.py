# myapp/models.py
from django.db import models

class MyFileModel(models.Model):
    file_name = models.CharField(max_length=100)
    uploaded_file = models.FileField(upload_to='uploads/' , null=True)
