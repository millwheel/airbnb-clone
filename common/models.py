from django.db import models


class CommonModel(models.Model):
    """
    Common Model Definition
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # This model is not added to db. This model is abstract model.
    class Meta:
        abstract = True # This is essential to use abstract
