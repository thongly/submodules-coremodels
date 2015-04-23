from django.db import models

# Create your models here.

class Article(models.Model):
	name = models.CharField(max_length=50)
	text = models.TextField()

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return '%s' % self.name
