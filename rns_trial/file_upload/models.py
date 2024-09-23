from django.db import models
from django_cryptography.fields import encrypt
from django.utils import timezone
# Create your models here.
class FileUpload(models.Model):
    uploaded_at = models.DateTimeField(default=timezone.now)
    file_upload = models.FileField()