from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=15)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="blog_images/")
    twitter = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)

    create_at = models.DateTimeField(auto_now_add=True)
    read_minute = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="article_images/")
    day = models.CharField(max_length=2)
    year = models.CharField(max_length=4)
    month = models.CharField(max_length=15)
    info = models.CharField(max_length=100)

    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title