from django.utils import timezone
from django.urls import reverse_lazy
from django.views import generic

from .models import Services


class Create(generic.CreateView):
    model = Services
    fields = '__all__'


class List(generic.ListView):

    model = Services
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class Detail(generic.DetailView):

    model = Services

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class Update(generic.UpdateView):
    model = Services
    fields = '__all__'


class Delete(generic.DeleteView):
    model = Services
    success_url = reverse_lazy('services:list')
