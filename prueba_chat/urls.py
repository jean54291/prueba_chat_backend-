"""prueba_chat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from modulos.usuarios.views import PersonAPI
from modulos.mensajes.views import MensajeApi
from rest_framework.authtoken import views

from api_login.api import Logout,Login
urlpatterns = [
    path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('login',Login.as_view()),
    path('logout',Logout.as_view()),
    path('api_generate_token/', views.obtain_auth_token),
    path('persona/create_persona/', PersonAPI.as_view(), name = "api_create_persona"),
    path('persona/lista_personas/', PersonAPI.as_view(), name = "api_lista_persona"),
    path('persona/update/<int:pk>/', PersonAPI.as_view(),  name = "api_actualizar_persona"),
    path('persona/detail/<int:pk>/', PersonAPI.as_view(), name = "api_detalle_persona"),
    path('mensajes/create_mensajes/', MensajeApi.as_view(), name = "api_create_mensaje"),
    path('mensajes/lista_mensajes/', MensajeApi.as_view(), name = "api_lista_mensaje"),
    path('mensajes/update/<int:pk>/', MensajeApi.as_view(),  name = "api_actualizar_mensaje"),
    path('mensajes/detail/<int:pk>/', MensajeApi.as_view(), name = "api_detalle_mensaje"),


]
