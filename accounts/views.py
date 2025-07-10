from academics.models import Course, Result
from django.db.models import Count
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import StudentRegisterForm
from .models import CustomUser

@login_required
def home(request):
    context = {}

    if request.user.role != 'student':
        total_students = CustomUser.objects.filter(role='student').count()
        total_courses = Course.objects.count()
        total_results = Result.objects.count()

        context = {
            'total_students': total_students,
            'total_courses': total_courses,
            'total_results': total_results,
        }

    return render(request, 'accounts/home.html', context)

@login_required
def register_student(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'student'
            user.save()
            return redirect('home')
    else:
        form = StudentRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
