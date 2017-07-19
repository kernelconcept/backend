"""kernel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  django_url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  django_url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  django_url(r'^blog/', include('blog.urls'))

Maintenant pour simplifier l'écriture d'url, on peut utiliser
    url('^home/{page}$') à la place de django_url(r'^home/(?P<page>[^/]+)$')
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url('^/', include('apps.kernelconcept.urls')),
    url('^admin/', admin.site.urls),
]
