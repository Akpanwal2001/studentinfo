# Generated by Django 3.2.7 on 2021-09-01 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_rename_addstudent_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Class',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='percentage',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='pincode',
            field=models.IntegerField(default=0),
        ),
    ]
