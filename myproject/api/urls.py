from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
  path('pizza_api',views.pizza_data_view, name="pizza_data_view"),
  path('pizza_api/<int:id>',views.pizza_data_edit_view, name="pizza_data_edit_view"),

]