from django.urls import path

from .views import RecommendationView

app_name = "recommendations"

urlpatterns = [
    path('recommendations/', RecommendationView.as_view())
]
