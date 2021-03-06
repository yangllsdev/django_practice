"""first_django_project URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from jd_like import views as views_jd_like
from guanyin import views as view_guanyin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^jd_like/', include("jd_like.urls", namespace="jd_like")),
    url(r'^chouti_like/', include("chouti_like.urls", namespace="chouti_like")),
    url(r'^guanyin/', include("guanyin.urls", namespace="guanyin")),
    url(r'^$', view_guanyin.index_home),
]
