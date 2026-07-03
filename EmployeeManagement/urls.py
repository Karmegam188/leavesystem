from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('employee.urls')),
    path('', include('accounts.urls')),
    path('leave/', include('leave_management.urls')),
    path('dashboard/', include('dashboard.urls')),
]