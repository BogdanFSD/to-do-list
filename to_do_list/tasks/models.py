from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    content = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    performance = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ("-performance", "-created")

    def __str__(self):
        return self.content
