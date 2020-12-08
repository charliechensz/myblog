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


# Create models for HongYe here.

class Cust(models.Model):
    cust = models.CharField(max_length=12, verbose_name='客户代码', help_text='不能输入客户名称，注意信息保密', default='- ')
    name = models.CharField(max_length=12, verbose_name='名字',default='- ')
class Shipment(models.Model):
    
    # 制定出货计划
    ship = models.CharField(max_length=12, verbose_name='出货单编号', unique=True, db_index=True)
    #cust = models.CharField(max_length=12,  verbose_name='客户代码', help_text='不能输入客户名称，注意信息保密', default='- ')
    belong = models.ForeignKey(Cust,on_delete=models.SET_NULL,related_name="ship_cust",null=True,blank=True)
    gongdi = models.CharField(max_length=12,  verbose_name='工地', default='- ')
    co = models.CharField(max_length=12,  verbose_name='销售单编号', default='- ')
    date = models.DateField(verbose_name='出货日期')  # auto_now=True
    item = models.CharField(max_length=12, verbose_name='产品编号', default='- ')

    qty = models.DecimalField(verbose_name='数量-方', max_digits=10, decimal_places=4, default=0)
    qty_tuo = models.DecimalField(verbose_name='数量-托', max_digits=10, decimal_places=4, default=0)
    truck = models.CharField(max_length=12, default='苏B-', verbose_name='车牌号')
    photo_ship = models.ImageField('出货单', upload_to='media', blank=True, null=True)

    # 叉车上货
    chache = models.CharField(max_length=12,  verbose_name='叉车工', default='- ')
    #photo = models.ImageField('照片', upload_to=user_directory_path, blank=True, null=True)
    photo_qian = models.ImageField('前面照片', upload_to='media', blank=True, null=True)
    photo_zuo1 = models.ImageField('左侧照片1', upload_to='media', blank=True, null=True)
    photo_zuo2 = models.ImageField('左侧照片2', upload_to='media', blank=True, null=True)
    photo_hou = models.ImageField('后面照片', upload_to='media', blank=True, null=True)
    photo_you1 = models.ImageField('右侧照片1', upload_to='media', blank=True, null=True)
    photo_you2 = models.ImageField('右侧照片2', upload_to='media', blank=True, null=True)
    # 门卫核准
    mengwei = models.CharField(max_length=12,  verbose_name='门卫', default='- ')
    text_ship = models.TextField(verbose_name='出厂备注', default='- ')

    # 托架回收
    qty_tuo_good = models.DecimalField(verbose_name='回收-好托架', max_digits=10, decimal_places=4, default=0)
    qty_tuo_bad = models.DecimalField(verbose_name='回收-坏托架', max_digits=10, decimal_places=4, default=0)
    photo_tuojia1 = models.ImageField('托架照片1', upload_to='media', blank=True, null=True)
    photo_tuojia2 = models.ImageField('托架照片2', upload_to='media', blank=True, null=True)
    photo_tuojia3 = models.ImageField('托架照片3', upload_to='media', blank=True, null=True)
    text_tuojia = models.TextField(verbose_name='托架回收备注', default='- ')

    # 其余。。
    create_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        managed = True
        verbose_name = "计划/叉车/门卫/托架回收.Name"
        verbose_name_plural = "1.计划/叉车/门卫/托架回收"

    def __str__(self):
        return self.ship
