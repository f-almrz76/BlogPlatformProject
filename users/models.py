from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='img', default="img/def.jpg")

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    title = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



