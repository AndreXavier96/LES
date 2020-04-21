from django.db import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class Campus(models.Model):
    nome = models.CharField(max_length=255)
    morada = models.TextField(blank=True, null=True)
    contacto = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus'


class Unidadeorganica(models.Model):
    nome = models.CharField(max_length=255)
    campus = models.ForeignKey(Campus, models.DO_NOTHING, db_column='campus')

    class Meta:
        managed = False
        db_table = 'unidadeorganica'


class Utilizadortipo(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utilizadortipo'

class Departamento(models.Model):
    nome = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'departamento'



class Utilizador(models.Model):
    utilizadortipo = models.ForeignKey('Utilizadortipo', models.DO_NOTHING)
    email = models.CharField(unique=True, max_length=255)
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    numero_telemovel = models.IntegerField()
    cartao_cidadao = models.IntegerField()
    deficiencias = models.CharField(max_length=255)
    permitir_localizacao = models.IntegerField()
    utilizar_dados_pessoais = models.IntegerField()
    validado = models.IntegerField(blank=True, null=True)
    unidadeorganica = models.ForeignKey(Unidadeorganica, models.DO_NOTHING, blank=True, null=True)
    departamento = models.ForeignKey(Departamento, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utilizador'

class Colaboracao(models.Model):
    colaborador = models.ForeignKey('Utilizador', models.DO_NOTHING)
    data_colaboracao = models.DateField()
    hora_inicio_colab = models.TimeField()
    hora_fim_colab = models.TimeField()
    percurso = models.IntegerField()
    sala_de_aula = models.IntegerField()
    tarefa_atribuida = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'colaboracao'

class Diaaberto(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=255)
    contacto = models.IntegerField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    limite_inscricao_atividades = models.IntegerField()
    limite_inscricao_participantes = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'diaaberto'
