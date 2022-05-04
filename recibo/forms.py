from django import forms

from .models import Recibo


class ReciboForm(forms.ModelForm):

    class Meta:
        model = Recibo
        fields = 'nome', 'email', 'cpf', 'telefone', 'endereco', 'servico', 'data', 'valor', 'observacao'






