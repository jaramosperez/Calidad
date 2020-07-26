from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Ambito
from caracteristicas.models import Caracteristica
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.


@method_decorator(login_required(), name='dispatch')
class AmbitoList(ListView):
    model = Ambito


@method_decorator(login_required(), name='dispatch')
class AmbitoDetail(DetailView):
    model = Ambito

    def get_context_data(self, **kwargs):
        context = super(AmbitoDetail, self).get_context_data(**kwargs)
        caracteristica_listado = Caracteristica.objects.filter(ambito_id=self.object.id)
        context['caracteristica_listado'] = caracteristica_listado

        return context

