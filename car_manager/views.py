from django.views import generic
from django.urls import reverse_lazy
from .models import Car


class CarMixin:
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('car_list')


class CarCreateView(CarMixin, generic.CreateView):
    pass


class CarListView(CarMixin, generic.ListView):
    pass


class CarDetailView(CarMixin, generic.DetailView):
    pass


class CarUpdateView(CarMixin, generic.UpdateView):
    pass


class CarDeleteView(CarMixin, generic.DeleteView):
    pass
