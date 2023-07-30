from django.contrib import admin
from journal.models import Journal

class JournalAdmin(admin.ModelAdmin):
    list_display = ['title','author','created_on','status',]
    list_filter = ['status']

admin.site.register(Journal, JournalAdmin)

