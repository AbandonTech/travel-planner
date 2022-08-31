from django.db import models


class BaseTripModel(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Trip(BaseTripModel):
    ...


class Location(BaseTripModel):
    scheduled_visit_date = models.DateTimeField('Scheduled Visit Date', blank=True, null=True)
    trips = models.ManyToManyField(Trip, blank=True, null=True)
