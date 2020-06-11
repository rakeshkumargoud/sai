from django.shortcuts import render

def hod_login(request):
    return render(request, "hod/hlogin.html")
