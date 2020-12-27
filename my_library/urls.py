from django.conf.urls import url
from book_management import views
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^my_index/$', views.index)
]
