from django.db import models

# Create your models here.
class Notificacao(models.Model):
    id = models.IntegerField(primary_key=True)
    conteudo = models.CharField(max_length=255)
    hora = models.TimeField()
    prioridade = models.IntegerField(blank=True, null=True)
    utilizador_env_id = models.ForeignKey(utilizadores, models.DO_NOTHING, db_column='id')
    utilizador_rec_id = models.ForeignKey(utilizadores, models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'notificacoes'