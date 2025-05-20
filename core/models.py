from django.db import models


class Legislator(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Bill(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=500)
    sponsor_id = models.BigIntegerField()

    def __str__(self):
        return self.title


class VoteResult(models.Model):
    VOTE_TYPES = (
        (1, "Supported"),
        (2, "Opposed"),
    )

    id = models.BigIntegerField(primary_key=True)
    legislator_id = models.BigIntegerField()
    vote_id = models.BigIntegerField()
    vote_type = models.IntegerField(choices=VOTE_TYPES)

    def __str__(self):
        return (
            f"Vote: {self.id} Legislator: {self.legislator_id} Type: {self.vote_type}"
        )


class Vote(models.Model):
    id = models.BigIntegerField(primary_key=True)
    bill_id = models.BigIntegerField()

    def __str__(self):
        return f"Vote {self.id} - Bill {self.bill_id}"
