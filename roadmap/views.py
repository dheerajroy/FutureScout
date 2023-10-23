from django.views.generic import FormView, DetailView
from django.urls import reverse
from .models import RoadMap
from .forms import SearchForm


class SearchView(FormView):
    form_class = SearchForm
    template_name = 'roadmap/search.html'

    def get_success_url(self):
        return reverse('roadmap:result', args=[self.request.POST.get('current_level')])


class ResultView(DetailView):
    model = RoadMap
    template_name = 'roadmap/result.html'
    context_object_name = 'result'

    def get_object(self, queryset=None):
        return RoadMap.objects.get(slug=self.kwargs.get('current_level'))
