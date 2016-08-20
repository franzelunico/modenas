from __future__ import unicode_literals
from django.db import models
from django import forms


class Document(models.Model):
    filename = models.CharField(max_length=100)
    docfile = models.FileField(upload_to='documents/')


class UploadForm(forms.Form):
    filename = forms.CharField(max_length=100)
    docfile = forms.FileField(label='Selecciona un archivo')
