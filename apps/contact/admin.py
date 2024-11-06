from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'name',
        'email',
        'web_site',
        'phone_number',
        'subject',
        'is_active',
        'created_at',
        'updated_at',
    )
    ordering = ('id',)
    search_fields = ('user__first_name', 'name', 'email', 'web_site', 'phone_number', 'subject')
    list_filter = ('user', 'name', 'email', 'web_site', 'phone_number', 'subject', 'is_active',)
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )