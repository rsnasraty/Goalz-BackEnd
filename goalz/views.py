from django.shortcuts import render
from rest_framework import viewsets          
from .serializers import GoalzSerializer      
from .models import Goalz                    

class GoalzView(viewsets.ModelViewSet):       
    serializer_class = GoalzSerializer         
    queryset = Goalz.objects.all()              