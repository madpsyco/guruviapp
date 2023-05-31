from django.urls import path
from . import views
urlpatterns = [
    path('classvideo1/', views.classvideo1, name='classvideo1'),
    path('loginhome/', views.loginhome, name='loginhome'),
    path('classvideo/<str:video>/', views.classvideo, name='classvideo'),

]