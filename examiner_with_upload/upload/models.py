
# models.py
from django.db import models

class UploadedFile(models.Model):
    pdf_file = models.FileField(upload_to='pdf_uploads/')


# Create your models here.
