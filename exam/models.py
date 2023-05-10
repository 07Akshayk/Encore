from django.db import models

class Exam(models.Model):
    name        = models.CharField(max_length=50)
    date        = models.DateField()
    venue       = models.CharField(max_length=100)
    provider    = models.CharField(max_length=50)
    logo        = models.ImageField(upload_to='exam/logo', blank=True)
    details     = models.TextField()
    link        = models.CharField(max_length=100)
    price       = models.IntegerField()
    points      = models.IntegerField()
    brochure    = models.FileField(upload_to='exam/brochure', blank=True)
    eligibility = models.CharField(max_length=50)   
    url         = models.URLField(max_length=200, blank=True)
    
    def __str__(self):
        return self.name