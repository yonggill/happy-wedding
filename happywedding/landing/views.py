from django.views.generic.base import TemplateView
from django.conf import settings


class IndexParentsView(TemplateView):
    template_name = "wedding_parents.html"


class IndexView(TemplateView):
    template_name = "wedding.html"