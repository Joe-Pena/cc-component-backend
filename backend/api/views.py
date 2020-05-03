from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RecSerializer
from .models import Recommendation


class RecommendationView(APIView):
    def get(self, request):
        recommendations = Recommendation.objects.all()
        data = RecSerializer(recommendations, many=True).data
        return Response(data)
