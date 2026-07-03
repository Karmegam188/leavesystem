from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from leave_management.models import Leave


@login_required
def dashboard_view(request):

    user = request.user

    # 🔥 ADMIN
    if user.role == 'admin':
        return redirect('/admin/')

    # 🔥 EMPLOYEE DASHBOARD
    if user.role == 'employee':
        leaves = Leave.objects.filter(employee=user)

        context = {
            'role': 'employee',
            'leaves': leaves,
            'total': leaves.count(),
            'approved': leaves.filter(status='approved').count(),
            'pending': leaves.filter(status='pending').count(),
            'rejected': leaves.filter(status='rejected').count(),
        }

        return render(request, 'dashboard/dash.html', context)

    # 🔥 MANAGER DASHBOARD
    if user.role == 'manager':
        leaves = Leave.objects.all()

        context = {
            'role': 'manager',
            'leaves': leaves,
            'total': leaves.count(),
            'approved': leaves.filter(status='approved').count(),
            'pending': leaves.filter(status='pending').count(),
            'rejected': leaves.filter(status='rejected').count(),
        }

        return render(request, 'dashboard/dash.html', context)