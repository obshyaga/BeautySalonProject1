from django.urls import path
from .views import *

urlpatterns = [
    path('', StartPageView.as_view(), name='start_page')
]