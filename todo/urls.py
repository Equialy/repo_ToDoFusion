
from django.urls import path
from todo import views

urlpatterns = [

    path('', views.home, name='home'),
    path('category/<slug:category_slug>/', views.category_name, name='category_name'),

]
