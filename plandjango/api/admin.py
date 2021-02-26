from django.contrib import admin
from .models import Plan

@admin.register(Plan)
class PlanModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'item']
