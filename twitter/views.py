from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Post, Comentario, Perfil
from .forms import PerfilForm, UserUpdateForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

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
    posts = Post.objects.all().order_by('-criado_em')
    
    perfil, _ = Perfil.objects.get_or_create(user=request.user)

    user_form = UserUpdateForm(instance=request.user)
    perfil_form = PerfilForm(instance=perfil)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        perfil_form = PerfilForm(request.POST, request.FILES, instance=perfil)

        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            return redirect('feed')

    return render(request, 'feed.html', {
        'posts': posts,
        'user_form': user_form,
        'perfil_form': perfil_form
    })
    
def perfil_publico(request, username):
    usuario = get_object_or_404(User, username=username)
    perfil = usuario.perfil
    posts = Post.objects.filter(autor=usuario).order_by('-criado_em')
    
    seguindo = False
    if request.user.is_authenticated:
        seguindo = perfil.seguidores.filter(id=request.user.id).exists()

    return render(request, 'feed.html', {
        'posts': posts,
        'perfil': perfil,
        'usuario_perfil': usuario,
        'perfil_view': True,
        'seguindo': seguindo
    })

def verificar_usuario(request):
    username = request.GET.get('username')
    existe = User.objects.filter(username=username).exists()#conferindo se existe username iguais
    return JsonResponse({'exists': existe})#retornar true ou false pro exists

def postar_tweet(request):
    if request.method == 'POST':
        conteudo = request.POST.get('conteudo')
        if conteudo:
            Post.objects.create(autor=request.user, conteudo=conteudo)
    return redirect('feed')  # redireciona para a página do feed

def curtir_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)#busca post com id
    if request.user in post.curtidas.all():#se o user ja curtiu remove
        post.curtidas.remove(request.user)
    else:
        post.curtidas.add(request.user)#se n curtiu add
    return redirect('feed')

def comentar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        texto = request.POST.get('texto')
        if texto:
            Comentario.objects.create(
                post=post,
                autor=request.user,
                texto=texto
            )
    return redirect('feed')

def seguir_usuario(request, username):
    usuario_para_seguir = get_object_or_404(User, username=username)
    perfil_para_seguir = usuario_para_seguir.perfil

    if request.user != usuario_para_seguir:
        if perfil_para_seguir.seguidores.filter(id=request.user.id).exists():
            perfil_para_seguir.seguidores.remove(request.user)
        else:
            perfil_para_seguir.seguidores.add(request.user)

    return redirect('perfil_publico', username=username)

def alterar_senha(request):
    if request.method == 'POST':
        senha_atual = request.POST.get('old_password')
        nova_senha1 = request.POST.get('new_password1')
        nova_senha2 = request.POST.get('new_password2')

        if not request.user.check_password(senha_atual):
            messages.error(request, "Senha atual incorreta.")
        elif nova_senha1 != nova_senha2:
            messages.error(request, "As novas senhas não coincidem.")
        else:
            request.user.set_password(nova_senha1)
            request.user.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, "Senha alterada com sucesso.")
            return redirect('feed')

    return redirect('feed')