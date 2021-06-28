from django.db import models
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.core.mail import EmailMessage

# Create your views here.
def loginview(request):
    return render(request,'login.html')

class  CreateProfile(CreateView):
    model=SellerProfile
    form_class=SellerProfileForm
    template_name='sellercreate.html'
    success_url=''
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Successfully Created Your Profile.')
        return super().form_valid(form)
class  CreateSell(CreateView):
    model=Sell
    form_class=SellForm
    template_name='sellercreate.html'
    success_url=''
    def form_valid(self, form):
        form.instance.sellerp = self.request.user.seller
        messages.success(self.request, 'Successfully Created Your Profile.')
        return super().form_valid(form)
def createsell(request):
    if request.method=="POST":
        form=SellForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            amount=form.cleaned_data['amount']
            sellerp=request.user.seller
            comission=amount*0.15
            instance.sellerp=sellerp
            instance.comission=comission
            if sellerp.boss:
                Aboss=sellerp.boss
                Alevel=amount*0.05
                instance.Alevel=Alevel
                instance.Aboss=Aboss
                if Aboss.boss:
                    Bboss=Aboss.boss
                    Blevel=amount*0.04
                    instance.Blevel=Blevel
                    instance.Bboss=Bboss
                    if Bboss.boss:
                        Cboss=Bboss.boss
                        Clevel=amount*0.03
                        instance.Clevel=Clevel
                        instance.Cboss=Cboss
                        if Cboss.boss:
                            Dboss=Cboss.boss
                            Dlevel=amount*0.02
                            instance.Dlevel=Dlevel
                            instance.Dboss=Dboss
            instance.save()
    else:
        form=SellForm()
    return render(request,'sellercreate.html',{'form':form})


# def createsell(request):
#     if request.method=="POST":
#         form=SellForm(request.POST)
#         if form.is_valid():
#             price=form.cleaned_data['amount']
#             print(price)
#             seller=request.user.seller
#             print(seller)
#             if not seller.boss:
#                 comission=float(price*0.15)
#                 print(comission)
#                 # print(seller.bossprofile.count())
#                 total_referal=seller.bossprofile.count()
#                 percentadd=0
#                 for i in range(total_referal+1):
#                     percentadd=percentadd+(i*5)
#                     count=1
#                 print(percentadd)
#                 for item in seller.bossprofille.all():
#                     total_referal=item.bossprofile.count()
#                     for i in range(total_referal+1):
#                         percentadd=percentadd+(i*4)
#                         count=2
#             if seller.boss:
#                 comission=float(price*0.15)
#                 print(comission)
#             email = EmailMessage(
#                 "you got commision",f'your commission is {comission}tk', to=['mdfahadhossain71@gmail.com']
#             )
#             email.send()
#     else:
#         form=SellForm()
#     return render(request,'sellercreate.html',{'form':form})

    
def createprofile(request):
    try:
        instance = SellerProfile.objects.get(user=request.user)
    except SellerProfile.DoesNotExist:
        instance = None
    if request.method=="POST":
        if instance:
            form = SellerProfileForm(
                request.POST,  instance=instance)
        else:
            form = SellerProfileForm(request.POST)
        # selp=form.cleaned_data['boss']
        # print(selp)
        if form.is_valid():
            # selp=form.cleaned_data['boss']
            # print(selp)
            profile_obj = form.save(commit=False)
            profile_obj.user = request.user
            profile_obj.save()
            messages.success(request,'successfully Saved')
            return redirect('home')
    else:
        # slp=SellerProfile.objects.get(user=request.user)
        form = SellerProfileForm(instance=instance)
    return render(request,'sellercreate.html',{'form':form})

def handlelogout(request):
    logout(request)
    return redirect('home')
