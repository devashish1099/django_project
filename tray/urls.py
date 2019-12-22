from django.urls import path

from . import views

app_name = 'tray'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:title_id>/', views.details , name='details'),
    path('<int:title_id>/like/', views.like , name='like'),

]