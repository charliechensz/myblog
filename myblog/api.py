'''
Author: your name
Date: 2020-11-26 16:03:43
LastEditTime: 2020-11-26 22:24:21
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /myblog/myblog/api.py
'''
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myblog.models import Classes, Userinfo
from myblog.toJson import Classes_data, Userinfo_data
 
@api_view(['GET','POST'])
def api_test(request):
    
    classes = Classes.objects.all()
    data = {
        'classes':[]
    }
    for c in classes:
        data_item = {
            'id' : c.id,
            'text' : c.text,
            'userlist' : []
        }
        userlist = c.userinfo_classes.all()
        for user in userlist:
            user_data = {
                'id':user.id,
                'nickName':user.nickName,
                'headImg':str(user.headImg)
            }
            data_item['userlist'].append(user_data)
        data['classes'].append(data_item)
    return Response(data)

    # classes = Classes.objects.all() 
    # classes_data = Classes_data(classes,many=True) 
    # userinfo = Userinfo.objects.all() 
    # #print(userinfo)
    # userinfo_data = Userinfo_data(userinfo,many=True) 
    # #print(userinfo_data)
    # print(userinfo_data.data)
    
    # data = {
    #     "classes": classes_data.data,
    #     "userinfo": userinfo_data.data
    # }
    #return Response({'data':data})
    

   
    # verison 2.1 
