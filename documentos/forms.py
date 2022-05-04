from django import forms

from .models import Recibos


class ReciboForm(forms.ModelForm):

    class Meta:
        model = Recibos
        fields = 'nome', 'email', 'cpf', 'telefone', 'endereco', 'servico', 'data', 'valor', 'observacao'






