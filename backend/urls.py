from django.contrib import admin
from django.urls import path, include                 
from rest_framework import routers                    
from goalz import views                            

router = routers.DefaultRouter()                      
router.register(r'goalz', views.GoalzView, 'goalz')     

urlpatterns = [
    path('admin/', admin.site.urls),         
    path('api/', include(router.urls))               
]