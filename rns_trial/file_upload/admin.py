from django.contrib import admin
from rns_trial.file_upload.models import FileUpload

# Register your models here.
class FileUploadAdmin(admin.ModelAdmin):
    readonly_fields = ['file_upload', 'uploaded_at']

admin.site.register(FileUpload, FileUploadAdmin)
