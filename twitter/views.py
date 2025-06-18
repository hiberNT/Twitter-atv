from django.shortcuts import render

def auth_view(request):
    return render(request, 'autentication.html')