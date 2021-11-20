from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name="home"),
    path('US/', views.US_Data, name="US"),
    path('EU/', views.EU_Data, name="EU"),
]
