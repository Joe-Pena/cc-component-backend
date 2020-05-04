from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RecSerializer
from .models import Recommendation


class RecommendationView(APIView):
    serializer_class = RecSerializer

    def get(self, request):
        queryset = Recommendation.objects.all()
        score = self.request.query_params.get('score', None)
        usage = self.request.query_params.get('usage', None)

        if score is not None and usage is not None:
            queryset = queryset.filter(credit_rating=score, card_type=usage)
        data = RecSerializer(queryset, many=True).data
        return Response(data)
