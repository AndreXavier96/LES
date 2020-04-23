from django.db import models

class Utilizadortipo(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utilizadortipo'

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

class Notificacao(models.Model):
    conteudo = models.TextField(blank=True, null=True)
    hora = models.DateTimeField()
    prioridade = models.IntegerField(blank=True, null=True)
    assunto = models.TextField(blank=True, null=True)
    utilizador_env = models.ForeignKey(Utilizador, models.DO_NOTHING, related_name='utilizador_env')
    utilizador_rec = models.ForeignKey(Utilizador, models.DO_NOTHING, related_name='utilizador_rec')

    class Meta:
        managed = False
        db_table = 'notificacoes'
