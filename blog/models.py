from tkinter.constants import CASCADE

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



class Blog_info(models.Model):
    image = models.ImageField(upload_to="blog_single_photos/")
    title = models.CharField(max_length=50)
    text = models.TextField()

    second_title = models.CharField(max_length=50)
    second_image = models.ImageField(upload_to="second_blog_single_photos/")
    second_text = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




class Tags(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Author(models.Model):
    image = models.ImageField(upload_to="author_images/")
    full_name = models.CharField(max_length=20)
    info = models.CharField(max_length=202)

    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name



class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    full_name = models.CharField(max_length=202)
    message = models.TextField()
    telephone = models.CharField(max_length=20)


    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.full_name


class Categories(models.Model):
    cat = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="category")
    name = models.CharField(max_length=20)

