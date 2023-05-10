from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import studentDetail
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

# add URL validators --> for link
# https://stackoverflow.com/questions/45994290/how-to-make-a-model-field-as-hyperlink-in-django-models
class Workshop(models.Model):
    class Mode_choices(models.TextChoices):
        ON      = 'Online', _('Online') 
        OF      = 'Offline', _('Offline') 
        
    class Interest_choices(models.TextChoices):
        DS      = 'DS', _('Data Science') 
        AI      = 'AI', _('Artificial Intelligence')
        BS      = 'BS', _('Business')
        DES     = 'DES', _('Design')
        ES      = 'ES', _('Embedded system')
        
    name        = models.CharField(max_length=50)
    mode        = models.CharField(max_length=20, choices=Mode_choices.choices, default=Mode_choices.ON)
    category    = models.CharField(max_length=50, choices=Interest_choices.choices, default=Interest_choices.AI)
    date        = models.DateField()
    venue       = models.CharField(max_length=100)
    provider    = models.CharField(max_length=50)
    logo        = models.ImageField(upload_to='workshop/logo', blank=True)
    details     = models.TextField()
    link        = models.URLField(max_length=200, blank=True)
    price       = models.IntegerField()
    points      = models.IntegerField()
    brochure    = models.FileField(upload_to='workshop/brochure', blank=True)
    # url         = models.URLField(max_length=200, blank=True)
    
    def __str__(self):
        return self.name

class Lecture(models.Model):
    class Mode_choices(models.TextChoices):
        ON      = 'Online', _('Online') 
        OF      = 'Offline', _('Offline') 
    class Interest_choices(models.TextChoices):
        DS      = 'DS', _('Data Science') 
        AI      = 'AI', _('Artificial Intelligence')
        BS      = 'BS', _('Business')
        DES     = 'DES', _('Design')
        ES      = 'ES', _('Embedded system')
        
    name        = models.CharField(max_length=50)
    mode        = models.CharField(max_length=20, choices=Mode_choices.choices, default=Mode_choices.ON)
    category    = models.CharField(max_length=50, choices=Interest_choices.choices, default=Interest_choices.AI)
    date        = models.DateField()
    venue       = models.CharField(max_length=100)
    provider    = models.CharField(max_length=50)
    logo        = models.ImageField(upload_to='lecture/logo', blank=True)
    details     = models.TextField()
    link        = models.CharField(max_length=100)
    price       = models.IntegerField()
    points      = models.IntegerField()
    brochure    = models.FileField(upload_to='lecture/brochure', blank=True)
    speaker     = models.CharField(max_length=50)
    url         = models.URLField(max_length=200, blank=True)
    
    def __str__(self):
        return self.name
        
class Competition(models.Model):
    class Mode_choices(models.TextChoices):
        ON      = 'Online', _('Online') 
        OF      = 'Offline', _('Offline') 
        
    class Interest_choices(models.TextChoices):
        DS      = 'DS', _('Data Science') 
        AI      = 'AI', _('Artificial Intelligence')
        BS      = 'BS', _('Business')
        DES     = 'DES', _('Design')
        ES      = 'ES', _('Embedded system')
        
    name        = models.CharField(max_length=50)
    mode        = models.CharField(max_length=20, choices=Mode_choices.choices, default=Mode_choices.ON)
    category    = models.CharField(max_length=50, choices=Interest_choices.choices, default=Interest_choices.AI)
    date        = models.DateField()
    venue       = models.CharField(max_length=100)
    provider    = models.CharField(max_length=50)
    logo        = models.ImageField(upload_to='competition/logo', blank=True)
    details     = models.TextField()
    link        = models.CharField(max_length=100)
    price       = models.IntegerField()
    points      = models.IntegerField()
    brochure    = models.FileField(upload_to='competition/brochure', blank=True)
    speaker     = models.CharField(max_length=50)
    url         = models.URLField(max_length=200, blank=True)
    
    def __str__(self):
        return self.name
class Certificate(models.Model):
    class Category_choices(models.TextChoices):
        WS      = 'Worshop', _('Worshop') 
        LEC     = 'Lecture', _('Lecture') 
        COMP    = 'Competition', _('Competition')
    students    = models.ForeignKey(User, on_delete=models.PROTECT, default=False, blank=True)
    category    = models.CharField(max_length=50 ,choices=Category_choices.choices, default=Category_choices.COMP)
    type_id     = models.IntegerField()
    certificate = models.FileField(upload_to='certificate', blank=False)
    
    def __str__(self):
        return self.category+" id "+str(self.type_id) 
    
class Point(models.Model):
    class Category_choices(models.TextChoices):
        WS      = 'Worshop', _('Worshop') 
        LEC     = 'Lecture', _('Lecture') 
        COMP    = 'Competition', _('Competition')
    students    = models.OneToOneField(User, on_delete=models.PROTECT, default=False, blank=True)
    category    = models.CharField(max_length=50 ,choices=Category_choices.choices)
    points      = models.IntegerField(default=0)
    cert_field  = models.ManyToManyField(Certificate)
    
    def __str__(self):
        return self.students.first_name