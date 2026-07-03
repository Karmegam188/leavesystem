from django.shortcuts import render, redirect
from .models import Leave
from django.contrib.auth.decorators import login_required

@login_required
def employee_dashboard(request):
    leaves = Leave.objects.filter(user=request.user)
    return render(request, 'leave/employee_dashboard.html', {'leaves': leaves})


@login_required
def apply_leave(request):
    if request.method == 'POST':
        reason = request.POST['reason']
        from_date = request.POST['from_date']
        to_date = request.POST['to_date']

        Leave.objects.create(
            user=request.user,
            reason=reason,
            from_date=from_date,
            to_date=to_date
        )
        return redirect('employee_dashboard')

    return render(request, 'leave/apply_leave.html')


@login_required
def manager_dashboard(request):
    leaves = Leave.objects.all()
    return render(request, 'leave/manager_dashboard.html', {'leaves': leaves})


@login_required
def approve_leave(request, id):
    leave = Leave.objects.get(id=id)
    leave.status = 'Approved'
    leave.save()
    return redirect('manager_dashboard')


@login_required
def reject_leave(request, id):
    leave = Leave.objects.get(id=id)
    leave.status = 'Rejected'
    leave.save()
    return redirect('manager_dashboard')