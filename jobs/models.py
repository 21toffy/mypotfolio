from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=30)
    summary = models.CharField(max_length=200)
    url = models.URLField(blank=False, null=False)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Jobs'
        