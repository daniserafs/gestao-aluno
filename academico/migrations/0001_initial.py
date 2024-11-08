# Generated by Django 5.1.2 on 2024-11-08 14:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Insira o nome do novo Campus', max_length=250, verbose_name='Insira o nome do Campus')),
            ],
        ),
        migrations.CreateModel(
            name='Ingresso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250, verbose_name='Insira a forma de ingresso')),
            ],
        ),
        migrations.CreateModel(
            name='Situacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Insira a nova situação disponivel para o aluno', max_length=250, verbose_name='Insira a nova situção')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Insira o nome do curso')),
                ('campus', models.ForeignKey(help_text='Escolha o campus em que o curso é ofertado', on_delete=django.db.models.deletion.CASCADE, to='academico.campi')),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Insira o nome completo do aluno', max_length=200, verbose_name='Nome Completo do Aluno')),
                ('cpf', models.CharField(help_text='Insira apenas os números sem caracteres especiais', max_length=11, verbose_name='CPF do aluno')),
                ('matricula', models.IntegerField()),
                ('dataNascimento', models.DateField()),
                ('anoIngresso', models.CharField(max_length=4, verbose_name='Insira o ano de ingresso do aluno')),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.campi')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.curso')),
                ('formaIngresso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.ingresso')),
                ('situacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.situacao')),
            ],
        ),
    ]
