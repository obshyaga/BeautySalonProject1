from commonf.simplification import simplified_path

from django.views.generic import *


class StartPageView(TemplateView):
    template_name = simplified_path('start_page')


