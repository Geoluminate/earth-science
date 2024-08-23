from django.views.generic import TemplateView
from geoluminate.plugins import PluginRegistry
from geoluminate.utils import icon

from .models import Point
from .views import PointDetailView

location = PluginRegistry(base=PointDetailView)


# LOCATION PLUGINS
@location.page("overview", icon=icon("overview"))
class PointOverview(PointDetailView, TemplateView):
    model = Point
    base_template = "location/location_detail.html"
    template_name = "geoluminate/plugins/map.html"
