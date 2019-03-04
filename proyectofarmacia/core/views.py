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
        # variables que voy a mandar al template
        usuario = 'usuario no registrado'
        # grupo_sala = False
        # grupo_farmacia = False
        
        # if 'sala' == str(request.user.groups.all()[0]):

        # if request.user.groups.filter(name='sala').exists():
        #     print('es un usuario de sala')
        #     grupo_sala = True
        # else:
        #     print('no es un usuario de sala')
        # if request.user.groups.filter(name='farmacia').exists():
        #     print('es un usuario de farmacia')
        #     grupo_farmacia = True
        # else:
        #     print('no es un usuario de farmacia')
        # print('el usuario es: ', request.user.username)

        # print('los grupos son: ', request.user.get_group_permissions())
        
        
        if request.user.username:
            usuario = request.user.username
        return render(request, self.template_name, {'usuario':usuario})


# class SamplePageView(TemplateView):
#     template_name = 'core/sample.html'


# class ArchivoPageView(TemplateView):
#     template_name = 'core/archivo.html'