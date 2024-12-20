from django.db import models
from django.contrib.auth.models import User


def get_default_user():
    responsables = []
    responsables.append(User.objects.get_or_create(username='non-spécifié'))
    return responsables


class Formation(models.Model):
    intitule    = models.CharField(max_length=100)
    description = models.TextField()
    responsable = models.OneToOneField(User,
                                       on_delete=models.SET_NULL,
                                       null=True,
                                       blank=True)

    def __str__(self):
        return self.intitule


class UE(models.Model):
    titre        = models.CharField(max_length=100)
    description  = models.TextField()
    horaires_cm  = models.IntegerField()
    horaires_td  = models.IntegerField()
    horaires_tp  = models.IntegerField()
    ects         = models.IntegerField()  # credits est un mot réservé
    formations   = models.ManyToManyField(Formation)
    responsables = models.ManyToManyField(User, default = get_default_user)

    def __str__(self):
        return self.titre


