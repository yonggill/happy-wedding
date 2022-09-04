from django.views.generic.base import TemplateView
from django.conf import settings


class IndexView(TemplateView):
    template_name = "wedding.html"