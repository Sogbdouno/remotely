from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,  name="home"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('create/', views.create, name="create"),
    path('delete/<int:job_id>', views.job_delete, name="delete"),
    path('update/<job_id>', views.job_update, name="edit"),

]