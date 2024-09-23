from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import mixins, viewsets, generics, filters, status, views  # noqa: F401
from rns_trial.file_upload.models import FileUpload
from .serializers import UploadFileSerializer
from cryptography.fernet import Fernet
from django.conf import settings
from django.core.files.base import ContentFile

f = Fernet(settings.ENCRYPT_KEY)

class UploadFileViewSet(ModelViewSet):
    queryset = FileUpload.objects.all()
    serializer_class = UploadFileSerializer

    def create(self, request, *args, **kwargs):
        file = request.data['file_upload']
        file_hehe = file.read()
        encrypted = f.encrypt(file_hehe)
        content_file = ContentFile(encrypted, name=str(file))
        FileUpload.objects.create(
            file_upload = content_file
        )

        return Response("File uploaded", status=status.HTTP_200_OK)
    

class FilesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = FileUpload.objects.order_by("id")
    serializer_class = UploadFileSerializer
    