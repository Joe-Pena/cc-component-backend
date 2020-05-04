from .models import Recommendation
from rest_framework import serializers


class RecSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recommendation
        fields = '__all__'
        read_only_fields = ['card1', 'card2']

    def to_representation(self, obj):
        data = super(RecSerializer, self).to_representation(obj)
        data['card1'] = obj.card1
        data['card2'] = obj.card2
        return data
