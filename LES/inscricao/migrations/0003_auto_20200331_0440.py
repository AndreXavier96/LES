# Generated by Django 3.0.4 on 2020-03-31 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscricao', '0002_escola_inscricao_test'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Inscricao_test',
        ),
        migrations.AlterModelOptions(
            name='inscricao',
            options={'managed': False},
        ),
    ]
