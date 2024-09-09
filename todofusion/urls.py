from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # AUTH
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginuser, name='loginuser'),

    # Todos
    path('current/', views.currenttodo, name='currenttodo'),
    path('done_tasks/', views.complete_tasks, name='complete_tasks'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('todocreate/', views.todocreate, name='todocreate'),
    path('todoread/<int:todo_pk>/', views.todoread, name='todoread'),
    path('todoread/<int:todo_pk>/done/', views.tododone, name='tododone'),
    path('todoread/<int:todo_pk>/delete/', views.tododelete, name='totoddelete'),
]
