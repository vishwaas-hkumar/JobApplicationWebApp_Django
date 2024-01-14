from django.contrib import admin
from .models import Form

#modifying Forms section in Admin
class FormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('date', 'occupation')
    ordering = ('first_name',) #-first_name for reverse
    readonly_fields = ('occupation',)

#registering class Form with admin interface
admin.site.register(Form, FormAdmin)
