from django.shortcuts import render
#from myblog.models import SiteInfo, Classes, Userinfo
from myblog.models import Userinfo

Users = Userinfo.objects.all()

for user in users:
    print(user.nickname)

# test 
# test B 1.0
print('git test 1.0  ')

