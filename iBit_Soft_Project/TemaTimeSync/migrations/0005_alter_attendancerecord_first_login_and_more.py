# Generated by Django 4.2.3 on 2024-08-27 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TemaTimeSync', '0004_alter_attendancerecord_user_delete_user'),
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
