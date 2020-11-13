from django.db import models


class Blogdata (models.Model):
    title = models.CharField(max_length=100)
    post_date = models.DateField()
    content = models.TextField(max_length=20000)

    def __str__(self):
        return self.title

