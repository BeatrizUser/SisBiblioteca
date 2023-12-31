# Generated by Django 4.1 on 2023-07-29 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0002_autor_editora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sistema.autor'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='editora',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sistema.editora'),
        ),
    ]
