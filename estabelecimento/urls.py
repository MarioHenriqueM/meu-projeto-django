from django.urls import path
from . import views

app_name = 'estabelecimento'

urlpatterns = [
    path('', views.lista_ofertas, name='lista_ofertas'),
    path('nova/', views.criar_oferta, name='criar_oferta'),
    path('editar/<int:id>/', views.editar_oferta, name='editar_oferta'),
    path('excluir/<int:id>/', views.excluir_oferta, name='excluir_oferta'),
]

