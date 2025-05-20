from django.db import models

class Legislator(models.Model):
    id = models.BigIntegerField(primary_key=True)  # ID único do legislador
    name = models.CharField(max_length=255)  # Nome do legislador

    def __str__(self):
        return self.name
    
class Bill(models.Model):
    id = models.BigIntegerField(primary_key=True)  # ID único para o projeto
    title = models.CharField(max_length=500)  # Título do projeto
    sponsor_id = models.BigIntegerField()  # Permitir valores nulos

    def __str__(self):
        return self.title

class VoteResult(models.Model):
    id = models.BigIntegerField(primary_key=True)  # ID único do voto
    legislator_id = models.BigIntegerField()  # ID do legislador (não relacionado diretamente ao Legislator)
    vote_id = models.BigIntegerField()  # ID da votação
    vote_type = models.IntegerField()  # Tipo de voto (ex.: 1 = a favor, 2 = contra)

    def __str__(self):
        return f"Vote {self.id} - Legislator {self.legislator_id} - Type {self.vote_type}"

class Vote(models.Model):
    id = models.BigIntegerField(primary_key=True)  # ID único da votação
    bill_id = models.BigIntegerField()  # ID do projeto de lei (não relacionado diretamente ao Bill)

    def __str__(self):
        return f"Vote {self.id} - Bill {self.bill_id}"