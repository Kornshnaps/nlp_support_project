from django.urls import path

from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('getJson/', views.getJsonPred, name = 'getJsonPred'),
    path('vote/', views.index22, name='index22'),
    path('refit_model/', views.refit,name = 'refit')
]