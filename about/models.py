from django.db import models


class Team(models.Model):
    mission = models.CharField(max_length=202)
    vision = models.CharField(max_length=202)
    value = models.CharField(max_length=202)
    video = models.FileField(upload_to="team_videos/")

    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mission


class Clients(models.Model):
    text = models.CharField(max_length=202)
    image = models.ImageField(upload_to="clients/")
    full_name = models.CharField(max_length=20)
    job = models.CharField(max_length=20)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name