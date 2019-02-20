from django.urls import path

# el siguiente impor no es necesario en vistas basadas en clases
# from . import views

from .views import PedidoListView, PedidoDetailView, PedidoCreate

pedidos_patterns = ([

    # vistas basadas en clases
    path('', PedidoListView.as_view(), name='pedidos'),
    path('<int:pk>/<slug:slug>/', PedidoDetailView.as_view(), name='pedido'),
    path('crear/', PedidoCreate.as_view(), name='crear')
    
    # vistas basadas en funciones:
    # path('', views.pedidos, name='pedidos'),
    # path('<int:pedido_id>/<slug:pedido_slug>/', views.pedido, name='pedido'),
], 'pedidos')