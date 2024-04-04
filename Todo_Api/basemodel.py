from django.db import models


class TimeBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("created_at") #ascending order
        abstract = True #Dont create db table