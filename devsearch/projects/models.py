import uuid

from django.db import models


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    demo_link = models.CharField(max_length=2000, blank=True, null=True)
    source_link = models.CharField(max_length=2000, blank=True, null=True)
    tags = models.ManyToManyField(to='Tag', blank=True, related_name='projects')
    vote_total = models.IntegerField(default=0, blank=True, null=True)
    vote_ratio = models.IntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


# noinspection PyUnresolvedReferences
class Review(models.Model):
    REVIEW_VOTE_TYPES = (
        ('up', 'Up vote'),
        ('down', 'Down vote'),
    )

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    # owner =
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reviews')
    body = models.TextField(blank=True, null=True)
    value = models.CharField(max_length=10, choices=REVIEW_VOTE_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.project.title} -> {self.value}'


class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
