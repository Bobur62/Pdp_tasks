# Generated by Django 3.1.7 on 2021-03-30 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciality',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
