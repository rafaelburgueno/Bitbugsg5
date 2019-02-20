# la siguiente linea es necesaria para las vistas basadas en clases
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# el siguiente impor no es necesario en vistas basadas en clases
#from django.shortcuts import render, get_object_or_404, get_list_or_404

from django.urls import reverse_lazy

from .models import Pedidos


# vistas basadoas en clases:
class PedidoListView(ListView):
    model = Pedidos


class PedidoDetailView(DetailView):
    model = Pedidos


class PedidoCreate(CreateView):
    model = Pedidos
    # en la siguiente lines se tienen que especificar los campos que el usuario podra crear
    fields = ['paciente','cama','insumos','urgencia']
    success_url = reverse_lazy('pedidos:pedidos')


# vistas basadas en funciones:
# def pedidos(request):
#     pedidos = get_list_or_404(Pedidos)
#     return render(request, 'pedidos/pedido_list.html', {'pedidos':pedidos})


# def pedido(request, pedido_id, pedido_slug):
#     pedido = get_object_or_404(Pedidos, id=pedido_id)
#     return render(request, 'pedidos/pedidos_detail.html', {'pedido':pedido})