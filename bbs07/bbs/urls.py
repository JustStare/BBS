"""bbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import re_path as url
from django.views.static import serve
from django.contrib import admin
from django.urls import path

from bbs import settings
from app import views

urlpatterns = [
    #后台管理
    url(r'^admin/', admin.site.urls),
    #用户首页
    url(r'^$', views.home,name='home'),
    url(r'^home/', views.home,name='home'),
    #注册
    url(r'^register/', views.register,name='register'),
    #邮箱注册
    url(r'^register_email/', views.register_email,name='register_email'),
    #暴露后端用户头像数据文件夹
    url(r'^media/(?P<path>.*)',serve,{'document_root':settings.MEDIA_ROOT}),
    #登录
    url(r'^login/', views.login,name='login'),
    #图片验证码
    url(r'^get_code/', views.get_code,name='get_code'),
    
    #修改用户头像
    url(r'^set/avatar/', views.set_avatar,name='set_avatar'),
    # 注销
    url(r'^logout/', views.logout,name='logout'),

    #添加文章
    url(r'^add/articel/', views.add_articel,name='add_articel'),
    #删除文章(新增)
    url(r'^delete/article/', views.delete_article,name='delete_article'),
    #编辑器上传图片接口
    url(r'^upload_image/', views.upload_image,name='upload_image'),
    #点赞点踩
    url(r'^up_or_down/',views.up_or_down),
     #评论接口
    url(r'^comment/', views.comment,name='comment'),   
    #用户后台文章管理
    url(r'^backend/', views.backend,name='backend'),
    
    
    #个人站点
    # url(r'^(?P<username>\w+)/$',views.site,name='site'),
    # #侧边栏的筛选功能
    # url(r'^(?P<username>\w+)/(?P<condition>|category|tag|archive)/(?P<param>.*)/',views.site),
    # #文章浏览页
    # url(r'^(?P<username>\w+)/article/(?P<article_id>\d+)/',views.article_detail),

    #################################################################################################


    url(r'^bbs/home/', views.home_site,name='bbs_home_site'),  #接口实现主页
    url(r'^bbs/register/', views.bbs_register,name='bbs_register'),#接口实现注册
    url(r'^bbs/get_code/', views.bbs_get_code,name='bbs_get_code'),#接口实现获取验证码
    url(r'^bbs/login/', views.bbs_login,name='bbs_login'),#接口实现登录
    url(r'^bbs/register_email/', views.bbs_register_email,name='bbs_register_email'),#接口实现邮箱验证码
    url(r'^bbs/logout/', views.bbs_logout,name='bbs_logout'),#接口实现注销
    url(r'^bbs/my_site/',views.bbs_my_site,name='bbs_my_site'),#接口实现我的帖子
    url(r'^bbs/up_or_down/',views.bbs_up_or_down),#接口实现点赞
    url(r'^bbs/comment/', views.bbs_comment,name='bbs_comment'),#接口实现评论
    url(r'^bbs/delete/article/', views.bbs_delete_article,name='bbs_delete_article'),#接口实现文章详情
    url(r'^bbs/add/article/', views.bbs_add_article,name='bbs_add_article'),#接口实现添加文章
    url(r'^bbs/add_myclass/',views.add_myclass,name='bbs_add_myclass'),    #接口实现添加班级
    url(r'^bbs/search_class/',views.search_class,name='bbs_search_class'),   #接口实现班级搜索
    url(r'^bbs/AI_PIL/', views.AI_PIL, name='bbs_AI_PIL'),#接口实现虚拟合影
    url(r'^bbs/new_comment/', views.comment_to_me, name='comment_to_me'),#接口实现最新回复


#文章浏览页
    url(r'^bbs/article/(?P<article_id>\d+)/',views.bbs_article_detail),








]
