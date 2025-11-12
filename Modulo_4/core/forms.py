# core/forms.py 
from django import forms 
from .models import Tarefa  # Importe o Model 
# Esta classe herda de 'ModelForm' 
class TarefaForm(forms.ModelForm): 
# A "mágica" acontece aqui, na classe 'Meta' 
    class Meta: 
# 1. Diga ao form qual Model ele deve usar 
        model = Tarefa 
# 2. Diga quais campos do Model devem virar campos no form 
# Nós só queremos que o usuário defina o 'titulo'. 
# 'concluida' (default=False) e 'criada_em' (auto_now_add=True) 
# serão preenchidos automaticamente pelo Model. 
        fields = ['titulo']