from django.views.generic import TemplateView, DetailView

from .models import Baner, AboutUs, Service


class HomePageView(TemplateView):

    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner'] = Baner.objects.first()
        context['about_us'] = AboutUs.objects.first()
        context['services'] = Service.objects.filter(show=True)
        return context


class ServiceDetailView(DetailView):
    model = Service
    template_name = "main/service_detail.html"
    context_object_name = "service"
