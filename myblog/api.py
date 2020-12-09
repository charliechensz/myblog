
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

