from django.urls import path
from .views import HomePageView, ServiceDetailView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("<slug:slug>", ServiceDetailView.as_view(), name="service_detail"),
]
