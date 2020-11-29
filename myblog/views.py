from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from myblog.models import SiteInfo, Classes, Userinfo
# 导包处理

# Create your views here.
def index(request):

    siteinfo = SiteInfo.objects.all()[0]   # first record
    classes = Classes.objects.all()   # get all records
    userlist = Userinfo.objects.all()  # get all user info
 
    data = {
        "siteinfo":siteinfo,   
        "classes":classes,
        "userlist":userlist,
    }  
    return render(request,'index.html',data)
 
def classes(request):
    siteinfo = SiteInfo.objects.all()[0]  
    classes = Classes.objects.all()   
    
    try:
        choosed_id = request.GET["id"]
        print('choosed_id :', choosed_id)
        choosed = Classes.objects.filter(id=choosed_id)  
        print('choosed :', choosed) 
        print(type(choosed))
    except:
        return redirect('/') 
    
    if choosed:
        userlist = Userinfo.objects.filter(belong=choosed[0])
    else:
        userlist = []
    print('userlist :', userlist) 
    
    data = { 
        "siteinfo":siteinfo,   
        "classes":classes,
        "userlist":userlist,
    }   
    return render(request,'classes.html',data)
 
