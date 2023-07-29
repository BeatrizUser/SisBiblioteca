"""Biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from sistema import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buscar_livro/', views.buscar_livro, name='buscar_livro'),
    path('realizar_emprestimo/<int:livro_id>/<int:pessoa_id>/', views.realizar_emprestimo, name='realizar_emprestimo'),
    path('finalizar_emprestimo/<int:emprestimo_id>/', views.finalizar_emprestimo, name='finalizar_emprestimo'),
    # Outras URLs do seu aplicativo, se houver...
]