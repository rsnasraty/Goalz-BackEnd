from rest_framework import serializers
from .models import Goalz

class GoalzSerializer(serializers.ModelSerializer):
  class Meta:
    model = Goalz
    fields = ('id', 'title', 'description', 'completed')