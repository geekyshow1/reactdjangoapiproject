from django.urls import path
from . import views
urlpatterns = [
    path('list/', views.PlanList.as_view()),
    path('create/', views.PlanCreate.as_view()),
    path('delete/<int:id>', views.PlanDestroy.as_view()),
]