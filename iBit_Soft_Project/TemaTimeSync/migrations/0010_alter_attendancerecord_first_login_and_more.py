# Generated by Django 4.2.3 on 2024-08-28 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TemaTimeSync', '0009_alter_attendancerecord_first_login_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancerecord',
            name='first_login',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='attendancerecord',
            name='last_logout',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
