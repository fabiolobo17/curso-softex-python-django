from django.db import models 
# Cada classe aqui é "traduzida" para uma tabela no banco de dados 
class Tarefa(models.Model): 
# Um campo de texto curto, com máximo de 200 caracteres 
    titulo = models.CharField(max_length=200) 
    # Um campo booleano (verdadeiro/falso), que por padrão é Falso 
    concluida = models.BooleanField(default=False) 
    criada_em = models.DateTimeField(auto_now_add=True) 
    # Um campo de data e hora.  
    # auto_now_add=True: Salva a data e hora EXATAMENTE quando o objeto é criado 
    # Este é um "método mágico" do Python. 
    # Ele diz ao Django como "chamar" um objeto Tarefa. 
    # Em vez de "Tarefa object (1)", ele mostrará o título da tarefa. 
    # Isso é EXTREMAMENTE útil no painel de administração. 
    def __str__(self): 
        return self.titulo
# Create your models here.
