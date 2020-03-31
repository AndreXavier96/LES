from django.db import models


class Inscricao(models.Model):
    # tutorial_title = models.CharField(max_length=200)
    # tutorial_content = models.TextField()
    # tutorial_published = models.DateTimeField("date published", default=datetime.now())
    inscricao_title = "inscricao"  # models.CharField(max_length=50)

    def __str__(self):
        return self.Inscricao_title
