# Generated by Django 4.2.4 on 2023-09-08 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='category',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
