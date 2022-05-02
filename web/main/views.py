from django.views.generic import TemplateView

from .models import Baner, AboutUs


class HomePageView(TemplateView):

    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner'] = Baner.objects.first()
        context['about_us'] = AboutUs.objects.first()
        return context
