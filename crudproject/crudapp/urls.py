from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    path('', views.student_list, name='student_list'),
    path('create/', views.student_create, name='student_create'),
    path('update/<int:id>/', views.student_update, name='student_update'),
    path('delete/<int:id>/', views.student_delete, name='student_delete'),
]
