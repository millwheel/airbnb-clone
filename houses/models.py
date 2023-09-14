from django.db import models


class House(models.Model):
    """Model house"""

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(
        verbose_name="price", help_text="Positive numbers only"
    )
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        default=True, help_text="Does this house allow pets?"
    )
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)
    categories = models.ForeignKey(
        "categories.Category", null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name
