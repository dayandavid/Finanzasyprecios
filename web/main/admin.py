from django.contrib import admin
from .models import Contact, SocialLink, Baner


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = ('address', 'email', 'phone_number', 'created_at', 'updated_at')

    readonly_fields = ('created_at', 'updated_at')

    list_display = ('email', 'phone_number', 'created_at', 'updated_at')


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    fields = ('name', 'url', 'created_at', 'updated_at')

    readonly_fields = ('created_at', 'updated_at')

    list_display = ('name', 'url', 'created_at', 'updated_at')


@admin.register(Baner)
class BanerAdmin(admin.ModelAdmin):
    fields = ('title', 'subtitle', 'image',
              'youtube_video', 'created_at', 'updated_at')

    readonly_fields = ('created_at', 'updated_at')

    list_display = ('title', 'subtitle', 'image', 'created_at', 'updated_at')
