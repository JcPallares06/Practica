"""
URL configuration for colegioecologico project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from apprecoleccion import views;

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.mostrarlogin),
    path('mostrarprincipal', views.mostrarprincipal),
    path('mostrarlistarcolegio', views.mostrarlistarcolegio),
    path('mostraragregarcolegio', views.mostraragregarcolegio),
    path('mostraractualizarcolegio/<int:nit>', views.mostraractualizarcolegio),
    path('mostrarlistaroperario', views.mostrarlistaroperario),
    path('mostraragregaroperario', views.mostraragregaroperario),
    path('mostraractualizaroperario/<int:codigo>', views.mostraractualizaroperario),
    path('mostrarlistarcaneca', views.mostrarlistarcaneca),
    path('mostraragregarcaneca', views.mostraragregarcaneca),
    path('mostraractualizarcaneca/<int:codigo>', views.mostraractualizarcaneca),
    path('mostrarlistarrecoleccion', views.mostrarlistarrecoleccion),
    path('mostraragregarrecoleccion', views.mostraragregarrecoleccion),
    path('mostraractualizarrecoleccion/<int:id>', views.mostraractualizarrecoleccion),
    path('insertarcanenca', views.insertarcaneca),
    path('insertaroperario', views.insertaroperario),
    path('insertarcolegio', views.insertarcolegio),
    path('actualizaroperario/<int:ndocumento>', views.actualizaroperario),
    path('actualizarcaneca/<int:codigo>', views.actualizarcaneca),
    path('actualizarcolegio/<int:nit>', views.actualizarcolegio),
    path('actualizarrecoleccion/<int:id>', views.actualizarrecoleccion),
    path('eliminaroperario/<int:codigo>', views.eliminaroperario),
    path('eliminarcaneca/<int:codigo>', views.eliminarcaneca),
    path('eliminarcolegio/<int:codigo>', views.eliminarcolegio),
    path('eliminarrecoleccion/<int:id>',views.eliminarrecoleccion),
    path('insertarrecoleccion',views.insertarrecoleccion),
    path('mostrarconsultas', views.mostrarconsultas),
    path('consultas',views.consultas),
    path('consultas4',views.consultas4),
    path('consultas5',views.consultas5),
    path('consultas7',views.consultas7),
    path('consultas8',views.consultas8),
    path('filtrarcolegios/<str:nombre>',views.filtrarcolegios)
]
