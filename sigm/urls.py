"""sigm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from principal.views import *

urlpatterns = [
    path('estaciones/adicionar/', estacion_add_view, name='estacion_add_view'),
    path('estaciones/modificar/<int:estacion_id>/', estacion_modify_view, name='estacion_modify_view'),
    path('estaciones/modificar/<int:estacion_id>/eliminar/', estacion_delete_view, name='estacion_delete_view'),
    path('rvm/adicionar/', rvm_add_view, name='rvm_add_view'),
    path('rvm/modificar/<int:rvm_id>/', rvm_modify_view, name='rvm_modify_view'),
    path('rvm/modificar/<int:rvm_id>/eliminar/', rvm_delete_view, name='rvm_delete_view'),
    path('iovmg/adicionar/', iovmg_add_view, name='iovmg_add_view'),
    path('iovmg/modificar/<int:iovmg_id>/', iovmg_modify_view, name='iovmg_modify_view'),
    path('iovmg/modificar/<int:iovmg_id>/eliminar/', iovmg_delete_view, name='iovmg_delete_view'),
    path('iovmp/adicionar/', iovmp_add_view, name='iovmp_add_view'),
    path('iovmp/modificar/<int:iovmp_id>/', iovmp_modify_view, name='iovmp_modify_view'),
    path('iovmp/modificar/<int:iovmp_id>/eliminar/', iovmp_delete_view, name='iovmp_delete_view'),
    path('pmp/adicionar/', pmp_add_view, name='pmp_add_view'),
    path('pmp/modificar/<int:pmp_id>/', pmp_modify_view, name='pmp_modify_view'),
    path('pmp/modificar/<int:pmp_id>/eliminar/', pmp_delete_view, name='pmp_delete_view'),
    path('pmg/adicionar/', pmg_add_view, name='pmg_add_view'),
    path('pmg/modificar/<int:pmg_id>/', pmg_modify_view, name='pmg_modify_view'),
    path('pmg/modificar/<int:pmg_id>/eliminar/', pmg_delete_view, name='pmg_delete_view'),
    path("login/", login_request, name="login"),
    path("logout/", cerrar_sesion, name="cerrar_sesion"),
    path("inicio/", admin_index, name="admin_index"),
    path('admin/', admin.site.urls),
    path('divulgacion/', index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
