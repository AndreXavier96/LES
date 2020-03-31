from django.db import models


class Escola(models.Model):
    nome = models.CharField(unique=True, max_length=255, blank=True, null=True)
    morada = models.TextField(blank=True, null=True)
    codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    contacto = models.IntegerField(blank=True, null=True)
    localidade = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'escola'


class Inscricao(models.Model):
    dia = models.DateField()
    escola = models.ForeignKey(Escola, models.DO_NOTHING, blank=True, null=True)
    estado = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inscricao'



