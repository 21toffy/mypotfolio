from django.db import models

class Services(models.Model):
    service_name= models.CharField(max_length=30)
    service_description= models.TextField()
    service_image = models.ImageField(upload_to="images/")


class About_Me(models.Model):
    image1 = models.ImageField(upload_to="images/", blank=True, null=True)
    image2 = models.ImageField(upload_to="images/", blank=True, null=True)
    about_me=models.TextField()


    def __str__(self):
        return self.about_me

        
