# la siguiente linea es necesaria para las vistas basadas en clases
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect

# el siguiente import no es necesario en vistas basadas en clases
#from django.shortcuts import render, get_object_or_404, get_list_or_404

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from .models import Pedidos
from pacientes.models import Paciente
from insumos.models import Insumo


class StaffRequiredMixin(object):
    """
    Este mixin requerira que el usuario sea miembro del staff
    """

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        # if not request.user.is_staff:
        #     return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


# vistas basadoas en clases:
class PedidoListView(ListView):
    model = Pedidos

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse_lazy('login'))
        
        return super(PedidoListView, self).dispatch(request, *args, **kwargs)


# vista de archivo
class ArchivoListView(ListView):
    model = Pedidos
    template_name_suffix = '_archivo'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse_lazy('login'))
        
        return super(ArchivoListView, self).dispatch(request, *args, **kwargs)



class PedidoDetailView(DetailView):
    model = Pedidos
    

#@method_decorator(staff_member_required, name='dispatch')
class PedidoCreate(CreateView):
    model = Pedidos
    # en la siguiente lines se tienen que especificar los campos que el usuario podra crear
    fields = ['paciente','cama','insumos','urgencia']
    # success_url = reverse_lazy('pedidos:pedidos')

    ###################################################
    # PRUEBO MANDAR UN CONTEXT DATA
    def get_context_data(self, **kwargs):
        context = super(PedidoCreate, self).get_context_data(**kwargs)
        context['pacientes'] = Paciente.objects.all()
        context['insumos'] = Insumo.objects.all()
        return context
    ###################################################


    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if 'sala' in request.user.groups.values_list('name', flat=True):
                return super(PedidoCreate, self).dispatch(request, *args, **kwargs)
            else:
                return redirect(reverse_lazy('home') + '?solo_para_usuarios_de_sala')
        else:
            return redirect(reverse_lazy('login') + '?debe_autentificarse_para_poder_acceder')


    def get_success_url(self):
        #return reverse_lazy('pedidos:procesar', args=[self.object.id]) + '?ok'
        return reverse_lazy('pedidos:crear') + '?creado'

    ########################################
    # VALIDAR FORMULARIOS
    def form_valid(self, form):
        #print(self.request.method)
        #print( self.request.user.username)
        if self.request.user.get_full_name():
            form.instance.solicitante = self.request.user.get_full_name()
        else:
            form.instance.solicitante = self.request.user.username
        #form.instance.solicitante = self.request.user.username
        return super().form_valid(form)
    ########################################


class PedidosUpdate(UpdateView):
    model = Pedidos
    #fields = ['procesante','estado','fecha_procesamiento','fecha_despachable']
    fields = ['estado','fecha_procesamiento','fecha_despachable']
    template_name_suffix = '_update_form'
    
    #success_url = reverse_lazy('pedidos:procesar')
    def get_success_url(self):
        #return reverse_lazy('pedidos:procesar', args=[self.object.id]) + '?ok'
        return reverse_lazy('pedidos:pedidos') + '?procesado'
    

    def dispatch(self, request, *args, **kwargs):
        
        if request.user.is_authenticated:
            if 'farmacia' in request.user.groups.values_list('name', flat=True):
                return super(PedidosUpdate, self).dispatch(request, *args, **kwargs)
            else:
                return redirect(reverse_lazy('home') + '?solo_para_usuarios_de_farmacia')
        else:
            return redirect(reverse_lazy('login') + '?debe_autentificarse_para_poder_acceder')
        
        # if not request.user.is_authenticated:
        #     return redirect(reverse_lazy('login'))
        # return super(PedidosUpdate, self).dispatch(request, *args, **kwargs)


    ########################################
    # VALIDAR FORMULARIOS
    def form_valid(self, form):
        if self.request.user.get_full_name():
            form.instance.procesante = self.request.user.get_full_name()
        else:
            form.instance.procesante = self.request.user.username
        #print(self.request.user.username)
        return super().form_valid(form)
    ########################################



class PedidosDelete(DeleteView):
    model = Pedidos
    #success_url = reverse_lazy('pedidos:pedidos')

    def get_success_url(self):
        return reverse_lazy('pedidos:pedidos') + '?borrado'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse_lazy('login'))
        return super(PedidosDelete, self).dispatch(request, *args, **kwargs)


# vistas basadas en funciones:
# def pedidos(request):
#     pedidos = get_list_or_404(Pedidos)
#     return render(request, 'pedidos/pedido_list.html', {'pedidos':pedidos})


# def pedido(request, pedido_id, pedido_slug):
#     pedido = get_object_or_404(Pedidos, id=pedido_id)
#     return render(request, 'pedidos/pedidos_detail.html', {'pedido':pedido})