from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm
from django.contrib.auth.models import User


# ================= LOGIN =================
def login_view(request):
    error = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_list')
        else:
            error = "Invalid username or password"

    return render(request, "login.html", {"error": error})


def logout_view(request):
    logout(request)
    return redirect('login')


def register_view(request):
    error = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            error = "Passwords do not match"
        elif User.objects.filter(username=username).exists():
            error = "Username already taken"
        else:
            User.objects.create_user(username=username, password=password1)
            return redirect('login')

    return render(request, "register.html", {"error": error})


# ================= CRUD =================

# READ
@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


# CREATE
@login_required
def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'student_form.html', {'form': form})


# UPDATE
@login_required
def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'student_form.html', {'form': form})


# DELETE
@login_required
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})
