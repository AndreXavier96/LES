import datetime

from django.db import models

from utilizadores.models import Utilizador, Campus, Faculdade, Departamento, UnidadeOrganica


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
    # estado = models.CharField(max_length=45, blank=True, null=True)
    hora_check_in = models.TimeField()
    unidadeorganica_checkin = models.ForeignKey(UnidadeOrganica, models.DO_NOTHING, db_column='unidadeorganica_checkin', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inscricao'

    def __str__(self):
        return self.id.__str__()


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
    data = models.DateField(blank=True, null=True)
    tipo_transporte = models.CharField(max_length=255)
    transporte_para_campus = models.CharField(max_length=255, null=True)
    transporte_entre_campus = models.CharField(max_length=255, null=True)
    inscricao = models.ForeignKey(Inscricao, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'transporteproprio'


class Percursos(models.Model):
    origem = models.CharField(max_length=255)
    destino = models.CharField(max_length=255)
    hora = models.TimeField()
    transporteproprio = models.ForeignKey(Transporteproprio, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'percursos'


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


# -------------------------------------------------------------------------------------

class Edificio(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=40)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Edificio'
        unique_together = (("nome", "campus"),)

    def __str__(self):
        return self.nome


class Sala(models.Model):
    id = models.AutoField(primary_key=True)
    identificacao = models.CharField(max_length=40)
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'Sala'
        unique_together = (("identificacao", "edificio"),)

    def __str__(self):
        return self.identificacao


class Tematica(models.Model):
    id = models.AutoField(primary_key=True)
    tema = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'Tematica'

    def __str__(self):
        return self.tema


class TipoAtividade(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'TipoAtividade'

    def __str__(self):
        return self.tipo


class PublicoAlvo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'PublicoAlvo'

    def __str__(self):
        return self.nome


class Sessao(models.Model):
    id = models.AutoField(primary_key=True)
    hora = models.TimeField(unique=True, null=True)

    class Meta:
        db_table = 'Sessao'

    def get_hora(self):
        return self.hora

    def __str__(self):
        return str(self.hora)


class Atividade(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    descricao = models.TextField(null=True)
    duracao = models.IntegerField()
    limite_participantes = models.IntegerField()
    tipo_atividade = models.ForeignKey(TipoAtividade, on_delete=models.CASCADE, null=True)
    publico_alvo = models.ManyToManyField(PublicoAlvo, related_name='publico_alvo')
    data = models.DateField(default=datetime.date.today)
    unidadeorganica = models.ForeignKey(UnidadeOrganica, on_delete=models.CASCADE, null=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True)
    REJEITADA = 'RJ'  # invalidada
    PENDENTE = 'PD'  # por validar
    VALIDADA = 'VD'  # validada
    VALIDACAO_CHOICES = [
        ('RJ', 'Rejeitada'),
        ('PD', 'Pendente'),
        ('VD', 'Validada'),
    ]
    validada = models.CharField(
        max_length=2,
        choices=VALIDACAO_CHOICES,
        default=PENDENTE,
    )
    tematicas = models.ManyToManyField(Tematica, related_name='temas')
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, null=True)
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE, null=True, blank=True)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, null=True, blank=True)
    tipo_local = models.CharField(max_length=255, null=True, blank=True)
    responsavel = models.ForeignKey(Utilizador, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        db_table = 'Atividade'

    def get_tipo(self):
        return self.tipo_atividade

    def get_tipo_local(self):
        return self.tipo_local if self.tipo_local else 'Local não especificado'

    def __str__(self):
        return self.nome


class SessaoAtividade(models.Model):
    atividade = models.ForeignKey(Atividade, related_name='sessao_atividade', on_delete=models.CASCADE, null=True)
    sessao = models.ForeignKey(Sessao, on_delete=models.SET_NULL, null=True)
    dia = models.DateField(null=True)
    numero_colaboradores = models.PositiveSmallIntegerField(default=0, blank=True)
    n_alunos = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'SessaoAtividade'
        unique_together = (("atividade", "sessao", "dia"),)

    def __str__(self):
        return self.atividade.nome


class SessaoAtividadeInscricao(models.Model):
    id = models.AutoField(primary_key=True)
    sessaoAtividade = models.ForeignKey(SessaoAtividade, related_name='sessoes', on_delete=models.CASCADE)
    inscricao = models.ForeignKey(Inscricao, related_name='inscricoes', on_delete=models.CASCADE)
    numero_alunos = models.IntegerField()

    class Meta:
        db_table = 'SessaoAtividadeInscricao'

    def __str__(self):
        return self.id
