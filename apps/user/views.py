from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser


def register_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        password = request.POST.get("password")

        if email and phone_number and first_name and last_name and password:
            user = CustomUser.objects.create_user(
                email=email,
                phone_number=phone_number,
                first_name=first_name,
                last_name=last_name,
                password=password
            )
            messages.success(request, "Muvaffaqiyatli ro'yxatdan o'tdingiz!")
            return redirect("login")
        else:
            messages.error(request, "Barcha maydonlarni to'ldiring.")

    return render(request, "register.html")

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            messages.success(request, "Muvaffaqiyatli tizimga kirdingiz!")
            return redirect("home")
        else:
            messages.error(request, "Email yoki parol noto'g'ri.")

    return render(request, "login.html")

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Muvaffaqiyatli chiqdingiz.")
    return redirect("login")