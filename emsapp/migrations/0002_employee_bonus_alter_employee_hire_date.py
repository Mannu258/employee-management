# Generated by Django 5.0.1 on 2024-01-09 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employee',
            name='hire_date',
            field=models.DateTimeField(),
        ),
    ]
