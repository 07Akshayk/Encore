from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
class studentDetail(models.Model):
    # class Programme_choices(models.TextChoices):
    #     BTECH   = 'BT', _('BTech')
    #     BARCH   = 'BR', _('BArch')
    #     DIPLOMA = 'DI', _('Diploma')
    #     OTHERS  = 'O', _('Others')

    class Gender_choices(models.TextChoices):
        MALE    = 'M', _('Male')
        FEMALE  = 'F', _('Female')
        
    # class Category_choices(models.TextChoices):
    #     GENERAL = 'G', _('General')
    #     SC      = 'SC', _('SC')
    #     ST      = 'ST', _('ST')
    #     OBC     = 'OBC', _('Other backward Classes')
    #     EWS     = 'EWS', _('Economically Weaker Section')
        
    class Classes_choices(models.TextChoices):
        A       = 'A', _('A')
        B       = 'B', _('B')
        C       = 'C', _('C')
        D       = 'D', _('D')
    
    class Interest_choices(models.TextChoices):
        DS      = 'DS', _('Data Science') 
        AI      = 'AI', _('Artificial Intelligence')
        BS      = 'BS', _('Business')
        DES     = 'DES', _('Design')
        ES      = 'ES', _('Embedded system')
        
    class Dept_choices(models.TextChoices):
        CS      = 'CS', _('Computer Science') 
        ME      = 'ME', _('Mechanical') 
        EC      = 'EC', _('Electronics')
        EEE     = 'EEE', _('Electrical')
        CH      = 'CH', _('Chemical')
        
    class Institution_choices(models.TextChoices):
        TKM     = 'tkm', _('TKM College of Engineering')
        CET     = 'cet', _('College of Engineering Trivandrum')
        GECT    = 'gect', _('GEC Thrissur') 
        GECK    = 'geck', _('GEC Kannur')
        RGR     = 'rgr', _('Rajagiri School of Engineering and Technology')
        GECBH   = 'gecbrt', _('Government Engineering College, Barton Hill')
        MACE    = 'mace', _('MACE Kothamangalam')
        
    #  foreign key is one to many relationships
    user     = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=12, blank=False)
    # Program by default is btech so there is no option 
    # programme= models.CharField(max_length=12, choices=Programme_choices.choices)
    course   = models.CharField(max_length=50, choices=Dept_choices.choices) # if its others then its courses
    clas     = models.CharField(max_length=50, choices=Classes_choices.choices)
    gender   = models.CharField(max_length=2, choices=Gender_choices.choices)
    avatar   = models.ImageField(upload_to='student', blank=True)
    interest = MultiSelectField(max_length=500, choices=Interest_choices.choices)
    rollno   = models.IntegerField()
    inst     = models.CharField(max_length=200, choices=Institution_choices.choices, default=Institution_choices.TKM)
    credit_es= models.IntegerField(default=0)
    credit_ac= models.IntegerField(default=0)
    # category = models.CharField(max_length=3, choices=Category_choices.choices)
    # income   = models.IntegerField()

    def __str__(self):
        return self.user.first_name
     
class facultyDetail(models.Model):
    class Dept_choices(models.TextChoices):
        CS      = 'CS', _('Computer Science') 
        ME      = 'ME', _('Mechanical') 
        EC      = 'EC', _('Electronics')
        EEE     = 'EEE', _('Electrical')
        CH      = 'CH', _('Chemical')
        
    class Institution_choices(models.TextChoices):
        TKM     = 'tkm124', _('TKM College of Engineering')
        CET     = 'cet124', _('College of Engineering Trivandrum')
        GECT    = 'gect123', _('GEC Thrissur') 
        GECK    = 'geck125', _('GEC Kannur')
        RGR     = 'rgr156', _('Rajagiri School of Engineering and Technology')
        GECBH   = 'gecbrt76', _('Government Engineering College, Barton Hill')
        MACE    = 'mace123', _('MACE Kothamangalam')
    
    user     = models.OneToOneField(User, on_delete=models.CASCADE)
    id_card  = models.ImageField(upload_to='faculty/idcard', blank=True)
    dept     = models.CharField(max_length=50, choices=Dept_choices.choices)
    inst_id  = models.CharField(max_length=100, choices=Institution_choices.choices)
    
class promoterDetail(models.Model):
    user     = models.OneToOneField(User, on_delete=models.CASCADE)
    logo     = models.ImageField(upload_to='promoter/logo', blank=True)
    link     = models.URLField(max_length=200, blank=False)
    
