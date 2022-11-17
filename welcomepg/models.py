from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
        
    contact_number=models.BigIntegerField(null=True)
    if contact_number != None:
        typeofusr = models.CharField(max_length=20)
    else:
        typeofusr = "admin"

    def _str_(self):
        return f"{self.username}"

class acts(models.Model):
    act_name=models.TextField()
    act_shname=models.CharField(max_length=5)
'''
class Allot(models.Model):

    contractor = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='contractor',unique=True)
    auditor = models.ForeignKey(User,on_delete=models.CASCADE,null = True,related_name='auditor')
    pass
class Auditor(User):
    auditor1 = models.OneToOneField(User,on_delete = models.CASCADE,related_name='auditors')

@receiver(post_save, sender=User)
def create_auditor(sender, instance, created, **kwargs):
    if created and User.objects.filter(typeofusr='Auditor'):
        Auditor.objects.create(auditor1=instance)

@receiver(post_save, sender=User)
def save_auditor(sender, instance, **kwargs):
    instance.profile.save()

class Subcontractor(User):
    contractor1 = models.OneToOneField(User,on_delete = models.CASCADE,related_name='contractors')

@receiver(post_save, sender=User)
def create_subcontractor(sender, instance, created, **kwargs):
    if created and User.objects.filter(typeofusr='Sub-Contractor'):
        Subcontractor.objects.create(contractor1=instance)

@receiver(post_save, sender=User)
def save_subcontractor(sender, instance, **kwargs):
    instance.profile.save()
'''

