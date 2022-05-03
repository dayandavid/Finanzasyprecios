from django.contrib import admin
from .models import Contact, SocialLink, Baner, AboutUs, Service, TeamMember, TeamMemberSocial


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


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    fields = ('title', 'subtitle', 'content', 'mision', 'vision',
              'image', 'created_at', 'updated_at')

    readonly_fields = ('created_at', 'updated_at')

    list_display = ('title', 'image', 'created_at', 'updated_at')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    fields = ('name', 'short_description', 'long_description', 'show',
              'slug', 'created_at', 'updated_at')

    prepopulated_fields = {"slug": ("name",)}

    readonly_fields = ('created_at', 'updated_at')

    list_display = ('name', 'created_at', 'updated_at', 'show')

    list_editable = ('show',)


class TeamMemberSocialInline(admin.TabularInline):
    model = TeamMemberSocial
    fk_name = 'team_member'


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    fields = ('name', 'position', 'list_order',
              'image', 'created_at', 'updated_at')

    readonly_fields = ('created_at', 'updated_at')

    list_display = ('name', 'position', 'list_order',
                    'created_at', 'updated_at')

    inlines = [
        TeamMemberSocialInline,
    ]
