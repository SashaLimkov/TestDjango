from django.urls import path

from . import views

app_name = 'tree'
urlpatterns = [
    path('', views.index, name='index'),
    path('info/<int:pk>', views.info, name="info")
]