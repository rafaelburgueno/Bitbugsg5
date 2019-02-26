from django.shortcuts import render

# importamos el TemplateView para implementar las vistas basadas en clases
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'core/home.html'

    # metodo para insertar el diccionario de contexto(datos de la base de datos) al template.
    # usar el metodo get() inabilita al metodo get_context_data()
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['titulo'] = "Texto introducido desde core.views, con el metodo get_context_data()"
    #     return context

    # otra forma de insertar diccionarios de contexto
    def get(self, request, *args, **kwargs):
        if 'sala' == str(request.user.groups.all()[0]):
            print('si que si')
        else:
            print('mmm no no')
        return render(request, self.template_name, {'texto':'Texto introducido desde core.views, con el metodo get()','titulo':'Aplicacion para pedidos en farmacias.'})


# class SamplePageView(TemplateView):
#     template_name = 'core/sample.html'


# class ArchivoPageView(TemplateView):
#     template_name = 'core/archivo.html'