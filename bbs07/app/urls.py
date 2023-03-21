from django.urls import re_path as url
from django.views.static import serve
from django.contrib import admin
from django.urls import path

from bbs import settings
from app import views


urlpatterns = [
    # 后台管理
    url(r'^admin/', admin.site.urls),

    # 用户首页
    url(r'^$', views.home, name='home'),
    url(r'^home/', views.home, name='home'),
    # 注册
    url(r'^register/', views.register, name='register'),
    # 暴露后端用户头像数据文件夹
    url(r'^media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
    # 登录
    url(r'^login/', views.login, name='login'),
    # 图片验证码
    url(r'^get_code/', views.get_code, name='get_code'),

    # 修改用户头像
    url(r'^set/avatar/', views.set_avatar, name='set_avatar'),
    # 注销
    url(r'^logout/', views.logout, name='logout'),

    # 添加文章
    url(r'^add/articel/', views.add_articel, name='add_articel'),
    # 删除文章(新增)
    url(r'^delete/article/', views.delete_article, name='delete_article'),
    # 编辑器上传图片接口
    url(r'^upload_image/', views.upload_image, name='upload_image'),
    # 点赞点踩
    url(r'^up_or_down/', views.up_or_down),
    # 评论接口
    url(r'^comment/', views.comment, name='comment'),
    # 用户后台文章管理
    url(r'^backend/', views.backend, name='backend'),

    # 个人站点
    url(r'^(?P<username>\w+)/$', views.site, name='site'),
    # 侧边栏的筛选功能
    url(r'^(?P<username>\w+)/(?P<condition>|category|tag|archive)/(?P<param>.*)/', views.site),
    # 文章浏览页
    url(r'^(?P<username>\w+)/article/(?P<article_id>\d+)/', views.article_detail),

]
