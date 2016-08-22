from django.conf.urls import url
from django.contrib import admin
from conversor import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index_page, name='index'),
    url(r'^ejemplo/$', views.ejemplo, name='ejemplo'),
]
