# core/urls.py 
from django.urls import path 
from . import views  # O '.' importa as 'views' do app atual 
urlpatterns = [ 
    # Quando a URL for a raiz (''), chame a função 'home' de 'views.py' 
    path('', views.home, name='home'), 
]