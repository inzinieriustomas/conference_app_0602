from django.contrib import admin

from conferences.models import Conference
from events.models import Event


class EventInline (admin.TabularInline):
    model =  Event
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'start_date', 'end_date']
    inlines = [EventInline]

# Register your models here.
admin.site.register( Conference, ConferenceAdmin)