from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
#用户表
class UserInfo(AbstractUser):
    phone = models.BigIntegerField(null=True,verbose_name='手机号',blank=True)
    #头像
    avatar = models.FileField(upload_to='avatar/',default='avatar/default.png',verbose_name='用户头像')

    #给avatar字段传文件对象，文件存储在avatar路径下，avatar值保存的是文件路径

    create_time = models.DateField(auto_now_add=True)

    blog = models.OneToOneField(to='Blog',null=True,on_delete = models.SET_NULL)

    class Meta:
        verbose_name_plural = '用户管理'
        # verbose_name = '用户表'

#博客表
class Blog(models.Model):
    site_name = models.CharField(verbose_name='站点名称',max_length=32)
    site_title = models.CharField(verbose_name='站点标题',max_length=32)
    #简单认识样式内部的原理操作
    site_theme = models.CharField(verbose_name='站点样式',max_length=32)  #存cs/js文件路径

    def __str__(self):
        return self.site_name
    class Meta:
        verbose_name_plural = '博客管理'
#分类表
class Category(models.Model):
    name = models.CharField(verbose_name='文章分类',max_length=32)
    #blog = models.ForeignKey(to='Blog', null=True,on_delete = models.SET_NULL)


    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = '分类管理'
#标签表
class Tag(models.Model):
    name = models.CharField(verbose_name='文章标签', max_length=32)
    blog = models.ForeignKey(to='Blog', null=True,on_delete = models.SET_NULL)

    def __str__(self):
        return self.name

#文章表
class Article(models.Model):
    title = models.CharField(verbose_name='文章标题',max_length=64)
    desc = models.CharField(verbose_name='文章简介',max_length=255)
    content = models.TextField(verbose_name='文章内容')
    create_time = models.DateField(auto_now_add=True)
    #create_time = models.DateTimeField(auto_now_add=True)

    #数据库设计优化
    up_num = models.BigIntegerField(verbose_name='点赞数',default=0)
    down_num = models.BigIntegerField(verbose_name='点踩数',default=0)
    comment_num = models.BigIntegerField(verbose_name='评论数',default=0)

    #外键字段
    blog = models.ForeignKey(to='Blog',null=True,on_delete = models.SET_NULL)
    category = models.ForeignKey(to='Category',null=True,on_delete = models.SET_NULL)
    tags = models.ManyToManyField(to='Tag',
                                  through='Article2Tag',
                                  through_fields=('article','tag')
                                  )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = '文章管理'

class Article2Tag(models.Model):
    article = models.ForeignKey(to='Article',on_delete = models.CASCADE)
    tag = models.ForeignKey(to='Tag',on_delete = models.CASCADE)

#顶踩表
class UpAndDown(models.Model):
    user = models.ForeignKey(to='UserInfo',on_delete = models.CASCADE)
    article = models.ForeignKey(to='Article',on_delete = models.CASCADE)
    is_up = models.BooleanField()
    class Meta:
        verbose_name_plural = '点赞情况'
#评论表
class Comment(models.Model):
    user = models.ForeignKey(to='UserInfo',on_delete = models.CASCADE)
    article = models.ForeignKey(to='Article',on_delete =  models.CASCADE)
    content = models.CharField(verbose_name='评论',max_length=255)
    #create_time = models.DateTimeField(auto_now_add=True)
    #comment_num = models.IntegerField(default=0)
    #up_num = models.IntegerField(default=0)
    #down_num = models.IntegerField(default=0)
    #自关联
    parent = models.ForeignKey(to='self',null=True,blank = True, on_delete =  models.CASCADE)
    def __str__(self):
        return self.content
    class Meta:
        verbose_name_plural = '评论管理'
#班级搜索表
class ClassesRecode(models.Model):
    name = models.CharField(verbose_name='姓名',max_length=32)
    Student_ID = models.CharField(verbose_name='学号',max_length=32)
    campus = models.CharField(verbose_name='校区',max_length=32)
    grade = models.CharField(verbose_name='年级',max_length=32)
    major = models.CharField(verbose_name='专业',max_length=32)
    education = models.CharField(verbose_name='学历',max_length=32)
    Class = models.CharField(verbose_name='班级',max_length=32)
    class_name = models.CharField(verbose_name='班级名',max_length=256)
#外键

    user = models.ForeignKey(to='UserInfo',null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.class_name+'  '+self.name
    class Meta:
        verbose_name_plural = '班级管理'

#消息表
# class message(models.Model):
#     msg = models.CharField(verbose_name='内容', max_length=255)
#     send_user = models.ForeignKey(to='UserInfo',on_delete = models.SET_NULL)
#     receive_user = models.ForeignKey(to='UserInfo', on_delete=models.SET_NULL)
#     create_time =  models.DateTimeField(verbose_name='私信时间')

