# Generated by Django 3.2.5 on 2022-11-28 20:53

from django.db import migrations, models
import futoalumni.image_check


class Migration(migrations.Migration):

    dependencies = [
        ('futoalumni', '0005_rename_name_business_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='bussines_photo',
            field=models.ImageField(blank=True, null=True, upload_to=futoalumni.image_check.business_files_directory),
        ),
        migrations.AddField(
            model_name='alumni',
            name='company_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='alumni',
            name='nature_of_biz',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Business',
        ),
    ]