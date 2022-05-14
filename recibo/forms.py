from django.forms import ModelForm
from .models import Financeiros
from funcionarios.models import Funcionario



class FinanceirosForm(ModelForm):


    class Meta:
        model = Financeiros
        fields = 'profissional', 'paciente', 'procedimento', 'servico', 'data', 'valor', 'observacao', 'recibo'

        def __init__(self, user=None, *args, **kwargs):
            super(FinanceirosForm, self).__init__(*args, **kwargs)






