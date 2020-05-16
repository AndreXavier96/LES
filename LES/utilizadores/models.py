from django.db import models


class Faculdade(models.Model):
    # Campos
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'faculdade'

    def __str__(self):
        return self.nome



class Departamento(models.Model):
    # Campos
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, unique=True)
    #faculdade = models.ForeignKey(Faculdade, on_delete=models.CASCADE)

    class Meta:
        db_table = 'departamento'

    def __str__(self):
        return self.nome


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

    def __str__(self):
        return self.nome
    class Meta:
        managed = False
        db_table = 'unidadeorganica'


class Utilizadortipo(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.tipo

    class Meta:
        managed = False
        db_table = 'utilizadortipo'


class Utilizador(models.Model):
    utilizadortipo = models.ForeignKey(Utilizadortipo, models.DO_NOTHING)
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

class UnidadeorganicaDepartamento(models.Model):
    unidade_organica = models.ForeignKey(Unidadeorganica, models.DO_NOTHING, db_column='unidade_organica')
    departamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='departamento')

    class Meta:
        managed = False
        db_table = 'unidadeorganica_departamento'

class Tarefa(models.Model):
    nome = models.CharField(max_length=45)
    descricao = models.TextField()
    tipo_tarefa = models.CharField(max_length=2)
    localizacao_grupo = models.TextField(blank=True, null=True)
    origem = models.CharField(max_length=255)
    destino = models.CharField(max_length=255, blank=True, null=True)
    horario = models.TimeField(blank=True, null=True)
    dia = models.DateField()
    #sessaoatividade = models.ForeignKey(SessaoAtividade, models.DO_NOTHING, blank=True, null=True)#import do models inscrição
    sessao_origem_id = models.IntegerField(blank=True, null=True)
    sessao_destino_id = models.IntegerField(blank=True, null=True)
    colaborador_id = models.IntegerField()
    grupo = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tarefa'


class Tematica(models.Model):
    tema = models.CharField(unique=True, max_length=255)

class UtilizadorTarefa(models.Model):
    tarefa = models.ForeignKey(Tarefa, models.DO_NOTHING)
    coordenador = models.ForeignKey(Utilizador, models.DO_NOTHING,related_name='1+')#
    colaborador = models.ForeignKey(Utilizador, models.DO_NOTHING, blank=True, null=True, related_name='2+')#
    colaboracao = models.ForeignKey(Colaboracao, models.DO_NOTHING)
    estado = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utilizador_tarefa'

