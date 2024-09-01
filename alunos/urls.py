
# alunos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro_aluno, name='cadastro_aluno'),
    path('listagem/', views.listagem_alunos, name='listagem_alunos'),
]


