from django.urls import path
from . import views

urlpatterns = [
    path('', views.Hello),
    path('About/', views.About),
    path('Hello/<str:username>', views.Hello),
    path('Projects/', views.Project),
]