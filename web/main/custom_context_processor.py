from .models import Contact, SocialLink


def global_context(request):
    return {
        'contact_info': Contact.objects.first(),
        'social_links': SocialLink.objects.all()
    }
