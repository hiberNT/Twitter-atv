from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def auth_view(request):
    mensagem = ''
    abrir_login = False  # usado para abrir modal de login automaticamente

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'register':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

            if User.objects.filter(username=username).exists():
                mensagem = 'Usuário já existe'
            else:
                User.objects.create_user(username=username, email=email, password=password)
                mensagem = 'Cadastro realizado com sucesso! Agora faça login.'

        elif form_type == 'login':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('/feed')
            else:
                mensagem = 'Usuário ou senha inválidos.'
                abrir_login = True  # abre modal de login se erro

    return render(request, 'autentication.html', {
        'mensagem': mensagem,
        'abrir_login': abrir_login
    })

@login_required
def feed_view(request):
    return render(request, 'feed.html')

def verificar_usuario(request):
    username = request.GET.get('username')
    existe = User.objects.filter(username=username).exists()
    return JsonResponse({'exists': existe})

