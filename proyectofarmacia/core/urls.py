from django.urls import path

# importamos las vistas basadas en clases para servir los templates
from .views import HomePageView, SamplePageView, ArchivoPageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('sample/', SamplePageView.as_view(), name="sample"),
    path('archivo/', ArchivoPageView.as_view(), name="archivo"),

]