'''
Author: your name
Date: 2020-11-26 17:00:56
LastEditTime: 2020-11-26 22:17:43
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /myblog/myblog/toJson.py
'''
from rest_framework import serializers
from myblog.models import Classes, Userinfo

class Classes_data(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Classes
        fields = '__all__'
        
class Userinfo_data(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Userinfo
        fields = '__all__'
        