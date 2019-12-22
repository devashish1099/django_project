from django.db import models

# Create your models here.

class Title(models.Model):
    title_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title_text


class Article(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    article_text = models.CharField(max_length=2000)
    

    def __str__(self):
        return self.article_text
    