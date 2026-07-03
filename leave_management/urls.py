from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.employee_dashboard, name='employee_dashboard'),
    path('apply/', views.apply_leave, name='apply_leave'),
    path('manager/', views.manager_dashboard, name='manager_dashboard'),
    path('approve/<int:id>/', views.approve_leave, name='approve_leave'),
    path('reject/<int:id>/', views.reject_leave, name='reject_leave'),
]