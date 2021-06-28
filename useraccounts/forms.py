from django import forms
from django.db.models import fields
from .models import *
from django.contrib.auth.models import User

class SellerProfileForm(forms.ModelForm):
    
    class Meta:
        model=SellerProfile
        exclude=('user',)
class SellForm(forms.ModelForm):
    
    class Meta:
        model=Sell
        fields=('amount',)
        # exclude=('sellerp','comission')
    # def __init__(self, id, *args, **kwargs):
    #     super(SellerProfileForm, self).__init__(*args, **kwargs)
    #     self.fields['boss'].queryset = SellerProfile.objects.exclude(id=id)