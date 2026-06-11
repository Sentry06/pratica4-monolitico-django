from django.db import models


class Tarefa(models.Model):

    STATUS_CHOICES = [
        ("nao_iniciado", "Não iniciado"),
        ("aprovado", "Aprovado"),
        ("paralisado", "Paralisado"),
        ("finalizado", "Finalizado"),
    ]
    # nao precisa colocar a ID
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="nao_iniciado"
    )

    def __str__(self):
        return self.nome