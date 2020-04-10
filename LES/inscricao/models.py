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


class Prato(models.Model):
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    descricao = models.TextField()

    class Meta:
        managed = False
        db_table = 'prato'

    def __str__(self):
        return self.tipo


class EmentaPratoInscricao(models.Model):
    ementa = models.ForeignKey(Ementa, models.DO_NOTHING)
    prato = models.ForeignKey(Prato, models.DO_NOTHING)
    inscricao = models.ForeignKey(Inscricao, models.DO_NOTHING)
    numero_aluno_normal = models.IntegerField(blank=True, null=True)
    numero_aluno_economico = models.IntegerField(blank=True, null=True)
    numero_outro_normal = models.IntegerField(blank=True, null=True)
    numero_outro_economico = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ementa_prato_inscricao'

    def __str__(self):
        return self.inscricao


class Transporteproprio(models.Model):
    data = models.DateField(auto_now_add=True)
    hora_chegada = models.TimeField()
    hora_partida = models.TimeField()
    tipo_transporte = models.CharField(max_length=255)
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
    turma = models.CharField(max_length=45)
    total_participantes = models.IntegerField(blank=True, null=True)
    total_professores = models.IntegerField(blank=True, null=True)
    autorizacao = models.CharField(max_length=45, blank=True, null=True)
    ficheiro_autorizacao = models.CharField(max_length=45, blank=True, null=True)
    numero_acompanhantes = models.IntegerField(blank=True, null=True)
    check_in = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utilizadorparticipante'

