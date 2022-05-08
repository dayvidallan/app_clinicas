from django import forms
from .models import Recibo, Financeiro
from funcionarios.models import Funcionario


class ReciboForm(forms.ModelForm):

    class Meta:
        model = Recibo
        fields = 'nome', 'email', 'cpf', 'telefone', 'endereco', 'servico', 'data', 'valor', 'observacao', 'recibo'


class FinanceiroForm(forms.ModelForm):

    class Meta:
        model = Financeiro
        fields = 'paciente', 'servico', 'data', 'valor', 'observacao', 'recibo'



