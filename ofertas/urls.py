<<<<<<< HEAD
from django.urls import path
from . import views

app_name = 'ofertas'

urlpatterns = [
    # Estabelecimento
    path("criar_oferta/", views.criar_oferta, name="criar_oferta"),
    path("minhas_ofertas/", views.minhas_ofertas, name="minhas_ofertas"),
    path("editar_oferta/<int:pk>/", views.editar_oferta, name="editar_oferta"),
    path("excluir_oferta/<int:pk>/", views.excluir_oferta, name="excluir_oferta"),

    # Instituição
    path("disponiveis/", views.ofertas_disponiveis, name="ofertas_disponiveis"),
    path("reservar/<int:pk>/", views.reservar_oferta, name="reservar_oferta"),
    path("minhas_reservas_instituicao/", views.minhas_reservas, name="minhas_reservas_instituicao"),
]
=======
"""
URL configuration for ofertas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('estabelecimento.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
>>>>>>> 0192b1b3112be76959dfe801e399f15bdea50dbc
