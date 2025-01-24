from django.db import models

from django.db import models

class Yonalish(models.Model):
    nom = models.CharField(max_length=100)
    aktiv = models.BooleanField(default=True)

    def __str__(self):
        return self.nom


class Fan(models.Model):
    nom = models.CharField(max_length=100)
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE)
    asosiy = models.BooleanField(default=False)

    def __str__(self):
        return self.nom


class Ustoz(models.Model):
    JINS_CHOICES = [
        ('erkak', 'Erkak'),
        ('ayol', 'Ayol'),
        ('boshqa', 'Boshqa'),
    ]

    DARJA_CHOICES = [
        ('Bakalavr', 'Bakalavr'),
        ('Magistr', 'Magistr'),
    ]

    ism = models.CharField(max_length=100)
    jins = models.CharField(max_length=10, choices=JINS_CHOICES)
    yosh = models.IntegerField()
    daraja = models.CharField(max_length=10, choices=DARJA_CHOICES)
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism