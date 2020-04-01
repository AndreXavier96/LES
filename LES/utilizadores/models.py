from django.db import models

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

class Utilizador(models.Model):
    utilizadortipo = models.ForeignKey('Utilizadortipo', models.DO_NOTHING)
    email = models.CharField(max_length=255)
    password_digest = models.CharField(max_length=255, blank=True, null=True)
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    numero_telemovel = models.IntegerField()
    cartao_cidadao = models.IntegerField()
    deficiencias = models.CharField(max_length=255)
    permitir_localizacao = models.IntegerField()
    utilizar_dados_pessoais = models.IntegerField()
    validado = models.IntegerField(blank=True, null=True)
    unidadeorganica = models.ForeignKey(Unidadeorganica, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utilizador'

class Utilizadortipo(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utilizadortipo'


class Utilizadorparticipante(models.Model):
    utilizador = models.ForeignKey(Utilizador, models.DO_NOTHING, db_column='utilizador')
    escola = models.IntegerField()
    area_estudos = models.CharField(max_length=45)
    ano_estudos = models.IntegerField()
    turma = models.CharField(max_length=45)
    total_participantes = models.IntegerField(db_column='total__participantes', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    total_professores = models.IntegerField(blank=True, null=True)
    autorizacao = models.CharField(max_length=45, blank=True, null=True)
    ficheiro_autorizacao = models.CharField(max_length=45, blank=True, null=True)
    numero_acompanhantes = models.IntegerField(blank=True, null=True)
    check_in = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utilizadorparticipante'



