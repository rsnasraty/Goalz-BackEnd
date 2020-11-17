# todo/admin.py

from django.contrib import admin
from .models import Goalz # add this

class GoalzAdmin(admin.ModelAdmin):  # add this
    list_display = ('title', 'description', 'completed') # add this

# Register your models here.
admin.site.register(Goalz, GoalzAdmin) # add this