from django.contrib import admin

# Register your models here.
from .models import Contact

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ["name", "mobile", "created", "updated"]

    class Meta:
        model = Contact

admin.site.register(Contact, ContactModelAdmin)
