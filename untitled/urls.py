"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from demo.views import Demo, Request, ver_request, RequestAdmin
from django.contrib import admin
from django.urls import path

admin.site.register(Request, RequestAdmin)
admin.site.site_header = "Receptor JSON"
admin.site.site_title = "Receptor JSON"

urlpatterns = [
    path('admin/', admin.site.urls),
    url(u'notification', Demo.as_view(), name='demo'),
    url(r'^admin/demo/request/ver_request$', ver_request,
            name='ver_request'),
]
