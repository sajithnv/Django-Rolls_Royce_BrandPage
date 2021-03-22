

"""new_project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls import url
from newapp1.views import f2,gallery

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^',include(('newapp1.urls','newapp1'),namespace='newapp12')),
    url(r'^',include(('account.urls','account'),namespace='account12')),
    url(r'^$',f2,name='home1'),
    url(r'^gallery/$',gallery,name='gallery1'),
]
