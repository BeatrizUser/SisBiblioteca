from django.db import models
from django.utils import timezone

class CategoriaLivro(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    edicao = models.CharField(max_length=50)
    isbn = models.CharField(max_length=20)
    ano_publicacao = models.PositiveIntegerField()
    categoria = models.ForeignKey(CategoriaLivro, on_delete=models.SET_NULL, null=True)
    num_copias_disponiveis = models.PositiveIntegerField(default=1)
    reservado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    matricula = models.CharField(max_length=20)
    contato = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField(default=timezone.now)
    data_devolucao_prevista = models.DateTimeField()
    data_devolucao_efetiva = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Empréstimo de '{self.livro}' para '{self.pessoa}'"

    def save(self, *args, **kwargs):
        if not self.data_devolucao_prevista:
            self.data_devolucao_prevista = self.data_emprestimo + timezone.timedelta(days=15)
        super().save(*args, **kwargs)
