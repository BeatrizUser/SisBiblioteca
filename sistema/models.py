from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class Autor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Editora(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class CategoriaLivro(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    STATUS_CHOICES = [
        ('Disponível', 'Disponível'),
        ('Emprestado', 'Emprestado'),
    ]
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    editora = models.ForeignKey(Editora, on_delete=models.SET_NULL, null=True)
    edicao = models.CharField(max_length=50)
    isbn = models.CharField(max_length=20)
    ano_publicacao = models.PositiveIntegerField()
    categoria = models.ForeignKey(CategoriaLivro, on_delete=models.SET_NULL, null=True)
    num_copias_disponiveis = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Disponível')

    def __str__(self):
        return self.titulo
    
    def emprestimo_realizado(self):
        if self.num_copias_disponiveis > 0:
            self.num_copias_disponiveis -= 1
            if self.num_copias_disponiveis == 0:
                self.status = 'Emprestado'
            self.save()
    
    def emprestimo_finalizado(self):
        if self.num_copias_disponiveis >= 0:
            self.num_copias_disponiveis += 1
            if self.num_copias_disponiveis > 0:
                self.status = 'Disponível'
            self.save()

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

@receiver(post_save, sender=Emprestimo)
def update_livro_status(sender, instance, **kwargs):
    livro = instance.livro
    if instance.data_devolucao_efetiva is None:
        # Empréstimo criado ou atualizado sem data de devolução efetiva, então ainda está em andamento
        livro.status = 'Emprestado'
        livro.num_copias_disponiveis -= 1
    else:
        # Empréstimo finalizado com data de devolução efetiva, então está disponível novamente
        livro.status = 'Disponível'
        livro.num_copias_disponiveis += 1
    livro.save()
