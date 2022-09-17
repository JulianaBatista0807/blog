from django.forms import ModelForm
from .models import Postagem

class FormularioPostagem(ModelForm):

    class Meta:
        model = Postagem
        fields = ['titulo', 'autor', 'email', 'conteudo','nota','comentario']
