from django.contrib import admin
from .models import AttendanceRecord, UserOffDay


# Register your models here.
@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'first_login', 'last_logout', 'total_hours_worked', 'is_late')


@admin.register(UserOffDay)
class UserOffDayAdmin(admin.ModelAdmin):
    list_display = ('user', 'off_day')
