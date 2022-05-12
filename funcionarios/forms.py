from django import forms
from .models import Funcionario



class FuncioarioForm(forms.ModelForm):

    class Meta:
        model = Funcionario
        fields = 'nome', 'user', 'clinica', 'cpl', 'cro', \
                 'especialidade', 'endereco', 'bairro', 'cidade', \
                 'estado', 'texto', 'apresent', 'email', 'nrTelCelular', 'upload' \
                 'imagem'


