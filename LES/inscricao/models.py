from django.db import models

from utilizadores.models import Utilizador


class Escola(models.Model):
    nome = models.CharField(unique=True, max_length=255, blank=True, null=True)
    morada = models.TextField(blank=True, null=True)
    codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    contacto = models.IntegerField(blank=True, null=True)
    localidade = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'escola'

    def __str__(self):
        return self.nome


class Inscricao(models.Model):
    dia = models.DateField(auto_now_add=True)
    escola = models.ForeignKey(Escola, models.DO_NOTHING, blank=True, null=True)
    estado = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inscricao'

    def __str__(self):
        return self.escola.__str__()


class Ementa(models.Model):
    dia = models.DateField(null=True, blank=True)
    preco_aluno_economico = models.DecimalField(max_digits=4, decimal_places=2)
    preco_aluno_normal = models.DecimalField(max_digits=4, decimal_places=2)
    preco_outro_economico = models.DecimalField(max_digits=4, decimal_places=2)
    preco_outro_normal = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ementa'

    def __str__(self):
        return "ementa"


class EmentaInscricao(models.Model):
    ementa = models.ForeignKey(Ementa, models.DO_NOTHING)
    inscricao = models.ForeignKey('Inscricao', models.DO_NOTHING)
    numero_aluno_normal = models.IntegerField(blank=True, null=True)
    numero_aluno_economico = models.IntegerField(blank=True, null=True)
    numero_outro_normal = models.IntegerField(blank=True, null=True)
    numero_outro_economico = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ementa_inscricao'

    def __str__(self):
        return self.inscricao


class Transporteproprio(models.Model):
    data = models.DateField(auto_now_add=True)
    hora_chegada = models.TimeField()
    hora_partida = models.TimeField()
    tipo_transporte = models.CharField(max_length=255)
    transporte_campus = models.IntegerField()
    inscricao = models.ForeignKey(Inscricao, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'transporteproprio'

    def __str__(self):
        return self.inscricao


class Utilizadorparticipante(models.Model):
    utilizador = models.ForeignKey(Utilizador, models.DO_NOTHING, db_column='utilizador')
    escola = models.ForeignKey(Escola, models.DO_NOTHING, db_column='escola')
    area_estudos = models.CharField(max_length=45)
    ano_estudos = models.IntegerField()
    check_in = models.IntegerField(blank=True, null=True)
    inscricao = models.ForeignKey(Inscricao, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'utilizadorparticipante'


class ParticipanteIndividual(models.Model):
    autorizacao = models.IntegerField()
    ficheiro_autorizacao = models.CharField(max_length=255)
    acompanhantes = models.IntegerField()
    participante = models.ForeignKey(Utilizadorparticipante, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'participante_individual'


class ParticipanteGrupo(models.Model):
    total_participantes = models.IntegerField()
    total_professores = models.IntegerField()
    turma = models.CharField(max_length=255)
    participante = models.ForeignKey(Utilizadorparticipante, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'participante_grupo'


# --------------------------------------------


class Campus(models.Model):
    nome = models.CharField(max_length=255)
    morada = models.TextField(blank=True, null=True)
    contacto = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus'

    def __str__(self):
        return self.nome


class Edicifio(models.Model):
    nome_edificio = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'edicifio'

    def __str__(self):
        return self.nome_edificio


class Localizacaoatividade(models.Model):
    campus = models.ForeignKey(Campus, models.DO_NOTHING, db_column='campus', blank=True, null=True)
    edificio = models.ForeignKey(Edicifio, models.DO_NOTHING, db_column='edificio', blank=True, null=True)
    andar = models.IntegerField(blank=True, null=True)
    sala = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'localizacaoatividade'


class Atividade(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    duracao = models.IntegerField()
    validada = models.IntegerField()
    tipo_atividade = models.TextField(blank=True, null=True)
    publico_alvo = models.CharField(max_length=45, blank=True, null=True)
    localizacao = models.ForeignKey(Localizacaoatividade, models.DO_NOTHING, db_column='localizacao', blank=True, null=True)
    docente = models.ForeignKey(Utilizador, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'atividade'

    def __str__(self):
        return self.nome


class Sessao(models.Model):
    hora_inicio = models.TimeField()

    class Meta:
        managed = False
        db_table = 'sessao'


class SessaoAtividade(models.Model):
    atividade = models.ForeignKey(Atividade, models.DO_NOTHING)
    sessao = models.ForeignKey(Sessao, models.DO_NOTHING)
    data = models.DateField()
    n_alunos = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sessao_atividade'

    def __str__(self):
        return self.sessao


class SessaoAtividadeInscricao(models.Model):
    sessao_atividade = models.ForeignKey(SessaoAtividade, models.DO_NOTHING,
                                         db_column='sessao-atividade_id')
    inscricao = models.ForeignKey(Inscricao, models.DO_NOTHING)
    numero_alunos = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sessao_atividade_inscricao'
