from django.db import models
from common.models import CommonModel


class Experience(CommonModel):
    """Experiences model definition"""

    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default="서울")

    name = models.CharField(max_length=250)
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    price = models.IntegerField()
    address = models.CharField(max_length=250)
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField()
    perks = models.ManyToManyField("experiences.Perk")
    categories = models.ForeignKey(
        "categories.Category", null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self) -> str:
        return self.name


class Perk(CommonModel):
    """What is included on an Experience"""

    name = models.CharField(
        max_length=100,
    )
    details = models.CharField(
        max_length=150,
        blank=True,
        default="",
    )
    explanation = models.TextField()

    def __str__(self) -> str:
        return self.name