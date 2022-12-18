from django.urls import path


from . import views

urlpatterns = [
    path('', views.initialisation_db, name='index'),
    path('/api', views.moni),
]