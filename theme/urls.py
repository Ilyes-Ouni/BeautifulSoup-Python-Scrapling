from django.urls import path
from . import views

urlpatterns = [
    path('smartphones/', views.get_smartphones, name='get_smartphones'),
    path('filterSmartphones/', views.filter, name='get_smartphones'),
    path('smartphones/<str:href>', views.get_smartphone, name='get_smartphone'),
]
