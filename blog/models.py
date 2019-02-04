from django.db import models
from django.conf import settings


class Topic(models.Model):
    title = models.CharField(max_length=100, blank=False, unique=True)
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.title


class PostQuerySet(models.QuerySet):
    pass


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)


class Post(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(null=False, blank=False)
    topic = models.ForeignKey(Topic, null=True, related_name="posts", on_delete=models.SET_NULL)
    updated = models.DateTimeField(auto_now=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    objects = PostManager()

    def __str__(self):
        return "{}".format(self.title)


class UserComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    content = models.TextField(null=False, blank=False, max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="commnets")

    def __str__(self):
        return "{}".format(self.content)
