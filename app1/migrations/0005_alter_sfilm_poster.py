# Generated by Django 3.2.9 on 2021-12-05 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_sfilm_tahun_rilis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sfilm',
            name='poster',
            field=models.ImageField(upload_to='images'),
        ),
    ]
