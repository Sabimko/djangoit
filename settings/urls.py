from django.urls import path
from settings.views import itpark

urlpatterns = [
    path("", itpark, name='itpark')
]