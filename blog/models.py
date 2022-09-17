from django.db import models
# Create your models here.

class Postagem(models.Model):
    titulo = models.CharField(max_length=80)
    autor = models.CharField(max_length=50) 
    email = models.EmailField()
    conteudo = models.TextField()
    data_publicacao = models.DateField(auto_now_add=True)
    nota = models.PositiveIntegerField()
    imagem = models.ImageField()