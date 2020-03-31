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

class Utilizadortipo(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utilizadortipo'

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