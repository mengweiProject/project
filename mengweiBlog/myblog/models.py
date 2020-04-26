from django.db import models

class Administrator(models.Model):
    a_name = models.CharField(max_length=200)
    a_pwd = models.CharField(max_length=12)
    c_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}--------{}'.format(self.a_name, self.c_date)

# Create your models here.
class User(models.Model):
    u_name = models.CharField(max_length=100)
    u_age = models.IntegerField()
    u_article_number = models.IntegerField(default=0)

    def __str__(self):
        return '{}, {}, {}'.format(self.u_name, self.u_age, self.u_article_number)

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=10000)
    pub_date = models.DateField(auto_now=True)

    def __str__(self):
        # return '{}--------{}--------{}--------{}'.format(self.id, self.title, self.content[50:100], self.pub_date)
        return '{}--------{}--------{}'.format(self.title, self.content, self.pub_date)