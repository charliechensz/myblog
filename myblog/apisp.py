'''
Author: Charlie
Date: 2020-12-08 A3,haha
LastEditTime: 2020-11-26 22:24:21
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /myblog/myblog/api.py
'''
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myblog.models import Cust,Shipment
#from myblog.toJson import Classes_data, Userinfo_data
 
@api_view(['GET','POST'])
def api_test(request):
    custs = Cust.objects.all()
    data = {
        'custs':[]
    }
    for cust in custs:
        data_item = {
            'cust' : cust.cust,
            'name' : cust.name,
            'shipments' : [],
            }
        shipments = cust.ship_cust.all()
        for sp in shipments:
            ship_data = {
                'ship' : sp.ship,
                'gongdi' : sp.gongdi,
                'item' : sp.item,
                'qty'  : sp.qty,
            }
            data_item['shipments'].append(ship_data)
        data['custs'].append(data_item)
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
