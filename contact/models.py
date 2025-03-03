from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=202)
    email = models.EmailField()
    phone = models.CharField(max_length=202)
    message = models.TextField()
    is_published = models.BooleanField(default=False)

    create_at = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name