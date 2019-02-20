"""proyectofarmacia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# hay que importar la funcion include
from django.urls import path, include
from pedidos.urls import pedidos_patterns

urlpatterns = [
    # se agrega un path a la raiz, con un include que cargara de la app core el fichero url
    path('', include('core.urls')),
    path('pedidos/', include(pedidos_patterns)),
    path('admin/', admin.site.urls),
]
