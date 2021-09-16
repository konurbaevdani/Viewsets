from django.urls import path
from review.views import *


urlpatterns = [
    path('review/', ReviewListView.as_view()),
    path('review/create/', CreateReviewView.as_view()),
    path('review/delete/<int:pk>/', DeleteReviewView.as_view()),
    path('review/update/<int:pk>/', UpdateReviewView.as_view())
]
