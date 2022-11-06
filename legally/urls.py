from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='legally-home'),
    path('services/', views.services, name='legally-services'),
    path('appointment', views.appointment, name='legally-appointment'),
    path('attorneys', views.attorneys, name='legally-attorneys'),
    path('search', views.search, name='legally-search'),
    path('filter', views.filter, name='legally-filter'),
]