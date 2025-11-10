from django.shortcuts import render
from .models import Tarefa
def home(request): 
    # 2. Use o ORM para buscar os dados! 
# Tarefa.objects.all() significa: "Pegue todas as linhas da tabela Tarefa" 
    todas_as_tarefas = Tarefa.objects.all() 
# 1. Crie seu dicionário de contexto 
    context = { 
        'nome_usuario': 'Fabio', 
        'tecnologias': ['Python', 'Django', 'Models', 'Admin'],
        'tarefas': todas_as_tarefas  # 4. Adicione as tarefas ao contexto 
    } 
# 2. Passe o 'context' como terceiro argumento do render() 
    return render(request, 'home.html', context) 