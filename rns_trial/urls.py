"""
URL configuration for rns_trial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework import routers

from rns_trial.file_upload.views import UploadFileViewSet, FilesViewSet
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
# router.register('upload_file', UploadFileViewSet, basename="upload_file")
router.register("files", FilesViewSet, basename="files")  # noqa: E501
router.register("upload_file", UploadFileViewSet, basename="upload_file")  # noqa: E501

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

