from django.shortcuts import render, redirect
from .forms import AlunoForm
from .models import Aluno

def home(request):
    return render(request, 'alunos/home.html')

def cadastro_aluno(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listagem_alunos')
    else:
        form = AlunoForm()
    
    context = {'form': form}
    return render(request, 'alunos/cadastro_aluno.html', context)

def listagem_alunos(request):
    alunos = Aluno.objects.all()
    context = {'alunos': alunos}
    return render(request, 'alunos/listagem_alunos.html', context)

