from __future__ import unicode_literals
from django.db import models
from django import forms


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/')


class UploadForm(forms.Form):
    docfile = forms.FileField(label='Selecciona un archivo')
