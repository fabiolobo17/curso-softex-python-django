from django.shortcuts import render, redirect  # 1. Importe o 'redirect' 
from .models import Tarefa 
from .forms import TarefaForm                 
def home(request): 
# 2. Importe nosso novo 'TarefaForm' 
# 3. Lógica de POST: Se o formulário foi enviado 
    if request.method == 'POST': 
# Cria uma instância do form e preenche com os dados do POST 
        form = TarefaForm(request.POST) 
         
        # 4. O Django valida os dados (max_length, etc.) 
        if form.is_valid(): 
            # 5. Salva o objeto no banco de dados! 
            form.save() 
             
            # 6. Redireciona de volta para a 'home' 
            # Isso é o Padrão "Post-Redirect-Get" (PRG) 
            return redirect('home') 
         
        # Se o form NÃO for válido, o código continua e  
        # o 'form' (com os erros) será enviado para o template 
     
    # 7. Lógica de GET: Se o usuário apenas visitou a página 
    else: 
        form = TarefaForm()  # Cria um formulário vazio 
 
    # 8. A busca de dados (fora dos 'ifs', pois é necessária sempre) 
    todas_as_tarefas = Tarefa.objects.all().order_by('-criada_em') # Ordena pelas mais novas 
 
    # 9. Atualize o contexto para incluir o formulário 
    context = { 
        'nome_usuario': 'Fabio', 
        'tecnologias': ['Python', 'Django', 'Models', 'Forms'], 
        'tarefas': todas_as_tarefas,   # 10. Envie o 'form' (vazio ou com erros) para o template 
    } 
     
    return render(request, 'home.html', context) 