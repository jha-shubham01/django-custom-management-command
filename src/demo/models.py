from django.db import models


class Car(models.Model):

    class ManufacturerChoices(models.TextChoices):
        TOYOTA = 'Toyota'
        HONDA = 'Honda'
        FORD = 'Ford'
        BMW = 'BMW'
        OTHER = 'Other'
    
    manufacturer = models.CharField(
        max_length=20,
        choices=ManufacturerChoices.choices,
        default=ManufacturerChoices.OTHER,
    )
    model_name = models.CharField(max_length=100)

    def __str__(self):
        return self.model_name