# Generated by Django 2.0.1 on 2018-01-26 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180126_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='upload',
            field=models.ImageField(upload_to='uploads/', verbose_name='文件缩略图'),
        ),
    ]
