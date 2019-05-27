"""chronic_illness_mgmt_3888 URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url('', include('home.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api/v1/', include('home.api.v1.urls')),
    url(r'^admin/', admin.site.urls),
]

admin.site.site_header = 'Chronic Illness Mgmt'
admin.site.site_title = 'Chronic Illness Mgmt Admin Portal'
admin.site.index_title = 'Chronic Illness Mgmt Admin'
