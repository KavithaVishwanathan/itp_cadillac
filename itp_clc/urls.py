"""itp_clc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from EB import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout_page),
    url(r'^register/$', views.register),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^thanks/$',views.thanks,name='thanks'),
    url(r'^register/success/$', views.success),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^historical-information$',views.historical),
    url(r'^historical-information/eldorado-brougham/',include('EB.urls')),
    url(r'^survivors-registory$',views.survivors),
    url(r'^survivors-registory/eldorado-brougham/',include('EB.urls')),
]
