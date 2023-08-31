from django.db import models


class House(models.Model):
    """Model house"""
    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(verbose_name="price", help_text="Positive numbers only")
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True, help_text="Does this house allow pets?")

    def __str__(self):
        return self.name