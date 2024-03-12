from django.contrib import admin
from reminders.models import Reminder

# Register your models here.


class ReminderAdmin(admin.ModelAdmin):
    list_display = ['date', 'time', 'message', 'reminder_type']

admin.site.register(Reminder, ReminderAdmin)
