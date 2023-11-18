from django.urls import path
from . import views
from .views import react_page

urlpatterns = [
    path('', views.home_page),
    path('test', views.test),

]