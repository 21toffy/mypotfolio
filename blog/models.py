from django.db import models
from django.utils import timezone
from django.urls import reverse



class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.PROTECT)
    title = models.CharField(max_length=500)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(null = True, blank = True)

    def get_absolute_url(self):
        return reverse('Post_detail', kwargs={'pk': self.pk})

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved(self):
        return self.comments.filter(approved_comments =True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    post = models.ForeignKey("Post", related_name='comments', on_delete = models.CASCADE)
    author = models.CharField(max_length=50)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    approved_comments = models.BooleanField(default=False)
    def get_absolute_url(self):
        return reverse('post_list', kwargs={'pk': self.pk})

    def approve(self):
        self.approved_comments = True
        self.save()

    def __str__(self):
        return self.text[:50]














