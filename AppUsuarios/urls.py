from django.urls import path
from .views import *

urlpatterns = [
    path('v1/persona', PersonaApiView.as_view()),
]