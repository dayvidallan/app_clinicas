from django import forms

from .models import Paciente, Consulta


class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = 'nome', 'email', 'cpf', 'rg', \
                 'data_nascimento', 'email', \
                 'telefone', 'endereco', \
                 'data_consulta', 'anamnesi', 'upload'


class ConsultaForm(forms.ModelForm):

    class Meta:
        model = Consulta
        fields = 'paciente', 'data_consulta', 'anamnesi', 'upload'