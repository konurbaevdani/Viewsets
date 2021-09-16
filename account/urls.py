from django.urls import path
from .views import (RegistrationView, ActivationView, LoginView)


urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='register-account'),
    path('activate/', ActivationView.as_view()),
    path('login/', LoginView.as_view()),
]