from django.db import models

# Create your models here.
class SiteInfo(models.Model):
    title = models.CharField(null=True,blank=True,max_length=50)
    logo = models.ImageField(upload_to='logo/',null=True,blank=True)
    def __str__(self):
        return self.title
    # 返回Title值

""" def __int__(self):
        return self.id
    #返回ID值， id是系统自动生成的字段    
""" 

# 课程分类
class Classes(models.Model):
    code = models.CharField(null=True,blank=True,max_length=10,verbose_name="课程代码")
    text = models.CharField(max_length=50)
    def __str__(self):
        return self.text
        #self.text

# 用户， 留意一对多关系的构建， belong， ForeignKey, on_delete等用法
# related_name ？；
class Userinfo(models.Model):
    nickName = models.CharField(null=True,blank=True,max_length=50)
    headImg = models.ImageField(upload_to='userinfo',null=True,blank=True)
    # models.Decimal   ---十进制小数类型 = decimal   必须指定整数位max_digits和小数位decimal_places
    hours = models.DecimalField(default=0,max_digits=10, decimal_places=2,verbose_name='累计学时')
    belong = models.ForeignKey(Classes,on_delete=models.SET_NULL,related_name="userinfo_classes",null=True,blank=True)
    def __str__(self):
        return self.nickName
