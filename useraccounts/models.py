from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.shortcuts import redirect
# Create your models here.
class SellerProfile(models.Model):
    name=models.CharField(max_length=100)
    user=models.OneToOneField(User,  on_delete=models.CASCADE, related_name='seller')
    boss=models.ForeignKey('self',  on_delete=models.CASCADE, related_name='bossprofile',blank=True, null=True)
    def __str__(self):
        return self.name


        
class Sell(models.Model):
    sellerp=models.ForeignKey(SellerProfile,on_delete=models.CASCADE,related_name='sells')
    amount=models.IntegerField()
    comission =models.FloatField()
    Alevel=models.FloatField(blank=True, null=True)
    Aboss=models.ForeignKey(SellerProfile,on_delete=models.CASCADE,related_name='abosscomission',blank=True, null=True)
    Blevel=models.FloatField(blank=True, null=True)
    Bboss=models.ForeignKey(SellerProfile,on_delete=models.CASCADE,related_name='bbosscomission',blank=True, null=True)
    Clevel=models.FloatField(blank=True, null=True)
    Cboss=models.ForeignKey(SellerProfile,on_delete=models.CASCADE,related_name='cbosscomission',blank=True, null=True)
    Dlevel=models.FloatField(blank=True, null=True)
    Dboss=models.ForeignKey(SellerProfile,on_delete=models.CASCADE,related_name='dbosscomission',blank=True, null=True)
    def __str__(self):
        return str(self.amount)
    