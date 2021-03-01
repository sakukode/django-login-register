from django.urls import path

# import class View
from .views import CustomLoginView, HomeView, CustomLogoutView, RegisterView, CustomPasswordChangeView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('password/change/', CustomPasswordChangeView.as_view(), name='password_change'),
]