from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Post, Comentario

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
    posts = Post.objects.all().order_by('-criado_em')  # Busca todos os posts, do mais novo pro mais antigo
    return render(request, 'feed.html', {'posts': posts})  # Envia os posts do models pro template

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
    return redirect('feed')  # Redireciona para o feed após comentar