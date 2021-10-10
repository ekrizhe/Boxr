from django.urls import path
from . import views

app_name = "build_pallet"
urlpatterns = [
    path('', views.index, name="index"),

]