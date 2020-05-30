from django.utils import timezone
from django.urls import reverse_lazy
from django.views import generic

from .models import Products


class Create(generic.CreateView):
    model = Products
    fields = '__all__'


class List(generic.ListView):

    model = Products
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class Detail(generic.DetailView):

    model = Products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class Update(generic.UpdateView):
    model = Products
    fields = '__all__'


class Delete(generic.DeleteView):
    model = Products
    success_url = reverse_lazy('inventories:list')
