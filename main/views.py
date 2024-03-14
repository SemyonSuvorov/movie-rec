from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def profile_view(request):
    return render(request, "main/profile.html")
