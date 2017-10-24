"""crepes_bretonnes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accueil$', views.home),
    url(r'^article/(?P<id_article>\d+)$', views.view_article),
    url(r'^article/(?P<year>\d{4})/(?P<month>\d{1,2})$', views.list_articles),
    url(r'^article/(?P<month>\d{1,2})/(?P<year>\d{4})$', views.list_articles),
    url(r'^date', views.date_actuelle, name='date_view'),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)$', views.additionne, name='addition_view'),
]
