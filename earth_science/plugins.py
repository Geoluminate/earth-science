from django.utils.translation import gettext as _
from geoluminate.plugins import contributor, dataset, project, sample


class Map:
    name = _("Explorer")
    icon = "map.svg"
    template_name = "core/plugins/map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["map_source_list"] = {}
        return context

    def serialize_dataset_samples(self, dataset):
        return None


@project.page()
class ProjectMap(Map):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for dataset in self.get_object().datasets.all():
            context["map_source_list"].update(self.serialize_dataset_samples(dataset))
        return context


@dataset.page()
class DatasetMap(Map):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["map_source_list"].update(self.serialize_dataset_samples(self.get_object()))

        return context


@contributor.page()
class ContributorSampleMap(Map):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for dataset in self.get_object().datasets.all():
            context["map_source_list"].update(self.serialize_dataset_samples(dataset))
        return context


sample.register_page(Map)