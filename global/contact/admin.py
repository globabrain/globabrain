from django.contrib import admin
from contact.models import ContactMessage

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','create_on']
    list_filter = ['name']
    search_Field = ['name', 'create_on']

admin.site.register(ContactMessage, ContactAdmin)