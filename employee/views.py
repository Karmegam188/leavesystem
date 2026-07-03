from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Employee


@login_required
def profile_view(request):
    if Employee.objects.filter(user=request.user).exists():
        employee = Employee.objects.get(user=request.user)
        return render(request, 'employee/profile_view.html', {'employee': employee})

    if request.method == 'POST':
        department = request.POST.get('department')
        designation = request.POST.get('designation')
        
        Employee.objects.create(
            user=request.user,
            department=department,
            designation=designation
        )

        return redirect('profile')

    return render(request, 'employee/profile_form.html')