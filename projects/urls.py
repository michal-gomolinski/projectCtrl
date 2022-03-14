from django.urls import path, include
from .views import LandingPage

app_name = 'projects'

urlpatterns = [
    path('', LandingPage.as_view(), name="landing-page")
]