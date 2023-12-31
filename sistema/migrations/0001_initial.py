# Generated by Django 3.2.20 on 2023-07-29 01:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaLivro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('matricula', models.CharField(max_length=20)),
                ('contato', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=100)),
                ('editora', models.CharField(max_length=100)),
                ('edicao', models.CharField(max_length=50)),
                ('isbn', models.CharField(max_length=20)),
                ('ano_publicacao', models.PositiveIntegerField()),
                ('num_copias_disponiveis', models.PositiveIntegerField(default=1)),
                ('status', models.CharField(choices=[('Disponível', 'Disponível'), ('Emprestado', 'Emprestado')], default='Disponível', max_length=20)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sistema.categorialivro')),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emprestimo', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_devolucao_prevista', models.DateTimeField()),
                ('data_devolucao_efetiva', models.DateTimeField(blank=True, null=True)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.livro')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.pessoa')),
            ],
        ),
    ]
