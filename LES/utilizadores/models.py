from django.db import models

class Faculdade(models.Model):
    nome = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'Faculdade'

class Departamento(models.Model):
    nome = models.CharField(unique=True, max_length=255)
    faculdade = models.ForeignKey(Faculdade, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamento'

class Campus(models.Model):
    nome = models.CharField(max_length=255)
    morada = models.TextField(blank=True, null=True)
    contacto = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus'

class UnidadeOrganica(models.Model):
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
    unidadeorganica = models.ForeignKey(UnidadeOrganica, models.DO_NOTHING, blank=True, null=True)
    departamento = models.ForeignKey(Departamento, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utilizador'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    utilizador = models.ForeignKey('Utilizador', models.DO_NOTHING, db_column='utilizador', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'

class Colaboracao(models.Model):
    colaborador = models.ForeignKey('Utilizador', models.DO_NOTHING)
    data_colaboracao = models.DateField(blank=True, null=True)
    hora_inicio_colab = models.TimeField(blank=True, null=True)
    hora_fim_colab = models.TimeField(blank=True, null=True)
    percurso = models.IntegerField(blank=True, null=True)
    sala_de_aula = models.IntegerField(blank=True, null=True)
    tarefa_atribuida = models.IntegerField(blank=True, null=True)

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
    unidade_organica = models.ForeignKey(UnidadeOrganica, models.DO_NOTHING, db_column='unidade_organica')
    departamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='departamento')

    class Meta:
        managed = False
        db_table = 'unidadeorganica_departamento'

class Tipoatividade(models.Model):
    tipo = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'TipoAtividade'

class Atividade(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    duracao = models.IntegerField()
    limite_participantes = models.IntegerField()
    data = models.DateField()
    validada = models.CharField(max_length=2)
    tipo_local = models.CharField(max_length=255, blank=True, null=True)
    campus = models.ForeignKey('Campus', models.DO_NOTHING, blank=True, null=True, related_name='1+')
    departamento = models.ForeignKey('Departamento', models.DO_NOTHING, blank=True, null=True,related_name='1+')
    edificio = models.ForeignKey('Edificio', models.DO_NOTHING, blank=True, null=True)
    responsavel = models.ForeignKey('Utilizador', models.DO_NOTHING, blank=True, null=True)
    sala = models.ForeignKey('Sala', models.DO_NOTHING, blank=True, null=True)
    tipo_atividade = models.ForeignKey('Tipoatividade', models.DO_NOTHING, blank=True, null=True)
    unidadeorganica = models.ForeignKey('UnidadeOrganica', models.DO_NOTHING, blank=True, null=True, related_name='1+')

    class Meta:
        managed = False
        db_table = 'Atividade'

class Sessao(models.Model):
    hora = models.TimeField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sessao'

class Sessaoatividade(models.Model):
    dia = models.DateField(blank=True, null=True)
    numero_colaboradores = models.PositiveSmallIntegerField()
    atividade = models.ForeignKey(Atividade, models.DO_NOTHING, blank=True, null=True)
    sessao = models.ForeignKey(Sessao, models.DO_NOTHING, blank=True, null=True)
    n_alunos = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'SessaoAtividade'
        unique_together = (('atividade', 'sessao', 'dia'),)


class Edificio(models.Model):
    nome = models.CharField(max_length=40)
    campus = models.ForeignKey('Campus', models.DO_NOTHING, related_name='1+')

    class Meta:
        managed = False
        db_table = 'Edificio'
        unique_together = (('nome', 'campus'),)

class Sala(models.Model):
    identificacao = models.CharField(max_length=40)
    edificio = models.ForeignKey(Edificio, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sala'
        unique_together = (('identificacao', 'edificio'),)

class Tarefa(models.Model):
    nome = models.CharField(max_length=45)
    estado = models.CharField(max_length=2, blank=True, null=True)
    descricao = models.TextField()
    tipo_tarefa = models.CharField(max_length=2)
    dia = models.DateField()
    colaborador = models.ForeignKey('Utilizador', models.DO_NOTHING, blank=True, null=True, related_name='1+')
    coordenador = models.ForeignKey('Utilizador', models.DO_NOTHING, blank=True, null=True, related_name='1+')
    colaboracao = models.ForeignKey(Colaboracao, models.DO_NOTHING, blank=True, null=True, related_name='1+')
    grupo = models.CharField(max_length=255)
    atividade = models.ForeignKey(Atividade, models.DO_NOTHING, blank=True, null=True)
    destino = models.ForeignKey(Sala, models.DO_NOTHING, blank=True, null=True, related_name='1+')
    localizacao_grupo = models.ForeignKey(Sala, models.DO_NOTHING, blank=True, null=True, related_name='1+')
    horario = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarefa'

class Tematica(models.Model):
    tema = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'Tematica'


class UtilizadorTarefa(models.Model):
    tarefa = models.ForeignKey(Tarefa, models.DO_NOTHING)
    coordenador = models.ForeignKey(Utilizador, models.DO_NOTHING, related_name='1+')
    colaborador = models.ForeignKey(Utilizador, models.DO_NOTHING, blank=True, null=True, related_name='1+')
    colaboracao = models.ForeignKey(Colaboracao, models.DO_NOTHING)
    estado = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utilizador_tarefa'

