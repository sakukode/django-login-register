from django.urls import path

# import semua class View untuk modul Category dan News
from .views import CustomLoginView, HomeView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('home/', HomeView.as_view(), name='home'),
]