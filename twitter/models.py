from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    curtidas = models.ManyToManyField(User, related_name='curtidas', blank=True)

    def total_curtidas(self):
        return self.curtidas.count()

    def __str__(self):
        return f'{self.autor.username} - {self.conteudo[:20]}'
    
class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.autor.username} comentou: {self.texto[:30]}'

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #imagem = models.ImageField(upload_to='perfil/', default='perfil/default.png')
    imagem = models.ImageField(upload_to='perfil/', null=True, blank=True)
    
    seguidores = models.ManyToManyField(User, related_name='seguindo', blank=True)

    def __str__(self):
        return f'{self.user.username} Perfil'
    
def criar_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)