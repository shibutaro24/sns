# Generated by Django 3.1.3 on 2022-12-15 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='avator',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
