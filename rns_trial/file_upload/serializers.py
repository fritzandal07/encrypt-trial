from rest_framework import serializers
from rns_trial.file_upload.models import FileUpload


class UploadFileSerializer(serializers.ModelSerializer):
    
    # file_upload = FileField()
    class Meta:
        model = FileUpload
        # read_only_fields = ('file_upload')
        fields = ['file_upload']
    