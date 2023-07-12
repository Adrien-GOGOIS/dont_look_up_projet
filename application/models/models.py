from django.db import models


class Asteroid(models.Model):
    asteroid_id = models.CharField(max_length=10, default="0")
    name = models.CharField(max_length=50, default="No name")
    diameter = models.FloatField(default=0, help_text="diameter in kilometers")
    close_approach_date = models.CharField(max_length=10, help_text="Date format : YYYY-MM-DD", default="0")
    miss_distance = models.BigIntegerField(help_text="distance in kilometers", default=0)

    def __str__(self):
        return self.name


class LatestApproach(models.Model):
    asteroid = models.ForeignKey(Asteroid, db_index=True, on_delete=models.CASCADE)
    date = models.CharField(max_length=10, db_index=True)
    distance = models.CharField(max_length=10, db_index=True)


class ImageOfTheDay(models.Model):
    date = models.CharField(max_length=10, db_index=True)
    explanation = models.CharField(max_length=10000, db_index=True)
    hdurl = models.CharField(max_length=100, db_index=True)
    title = models.CharField(max_length=50, db_index=True)
    url = models.CharField(max_length=100, db_index=True)