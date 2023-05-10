from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField

class Scholarship(models.Model):
    class Programme_choices(models.TextChoices):
        BTECH   = 'BT', _('BTech')
        BARCH   = 'BR', _('BArch')
        DIPLOMA = 'DI', _('Diploma')
        OTHERS  = 'O', _('Others')

    class Gender_choices(models.TextChoices):
        MALE    = 'M', _('Male')
        FEMALE  = 'F', _('Female')
        
    class Category_choices(models.TextChoices):
        GENERAL = 'G', _('General')
        SC      = 'SC', _('SC')
        ST      = 'ST', _('ST')
        OBC     = 'OBC', _('Other backward Classes')
        EWS     = 'EWS', _('Economically Weaker Section')
        
    name                 = models.CharField(max_length=50)
    date                 = models.DateField()
    provider             = models.CharField(max_length=50)
    logo                 = models.ImageField(upload_to='scholarship/logo', blank=True)
    details              = models.TextField()
    link                 = models.CharField(max_length=100)
    income_eligibility   = models.IntegerField()
    program_eligibility  = MultiSelectField(max_length=100, choices=Programme_choices.choices)
    category_eligibility = MultiSelectField(max_length=100, choices=Category_choices.choices)
    gender_eligibility   = MultiSelectField(max_length=100, choices=Gender_choices.choices)
    
    def __str__(self):
        return self.name