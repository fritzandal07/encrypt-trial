# Generated by Django 4.2.16 on 2024-09-22 06:11

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('file_upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='file_upload',
            field=django_cryptography.fields.encrypt(models.FileField(upload_to='')),
        ),
    ]
