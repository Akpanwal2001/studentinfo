# Generated by Django 3.2.7 on 2021-09-01 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_rename_pin_addstudent_pincode'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Addstudent',
            new_name='Student',
        ),
    ]