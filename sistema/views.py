from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Livro, Pessoa, Emprestimo

def cadastrar_livro(request):
    if request.method == 'POST':
        # Processar os dados do formulário de cadastro de livro
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        editora = request.POST['editora']
        # ... outros campos do livro ...
        
        Livro.objects.create(titulo=titulo, autor=autor, editora=editora)
        
        return redirect('listar_livros.html')
    
    return render(request, 'cadastrar_livro.html')

def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'listar_livros.html', {'livros': livros})

def realizar_emprestimo(request, livro_id, pessoa_id):
    livro = get_object_or_404(Livro, id=livro_id)
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)

    if livro.num_copias_disponiveis > 0:
        Emprestimo.objects.create(livro=livro, pessoa=pessoa, data_emprestimo=timezone.now())
        livro.num_copias_disponiveis -= 1
        livro.save()
        
        return redirect('pagina_de_sucesso.html')
    else:
        return redirect('pagina_de_erro.html')

def finalizar_emprestimo(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)

    if not emprestimo.data_devolucao_efetiva:
        emprestimo.data_devolucao_efetiva = timezone.now()
        emprestimo.save()

        livro = emprestimo.livro
        livro.num_copias_disponiveis += 1
        livro.save()

    return redirect('pagina_de_sucesso.html')
