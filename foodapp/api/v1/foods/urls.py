from django.urls import path
from api.v1.foods.views import foods, singleFood, create, delete, update
from django.http import HttpResponse


urlpatterns = [
    path("",foods),
    path("view/<int:pk>/",singleFood),
    path("create/",create),
    path('delete/<int:pk>/',delete),
     path('update/<int:pk>/',update),
] 
