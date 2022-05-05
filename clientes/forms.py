from django import forms

from .models import Paciente


class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = 'nome', 'email', 'cpf', 'rg', \
                 'data_nascimento', 'email', \
                 'telefone', 'endereco', \
                 'data_consulta', 'anamnesi'


