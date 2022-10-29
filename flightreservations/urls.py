from .views import FlightDetail
from django.urls import path

urlpatterns = [
    path('Flight',FlightDetail.as_view(),name = 'detailcreate'),
    path('Registration',FlightDetail.as_view(),name = 'detailcreate'),
]
