from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app import models

admin.site.site_title = "后台管理"

admin.site.site_header = "后台管理"

admin.site.index_title = "后台管理"
#admin注册表
admin.site.register(models.UserInfo,UserAdmin)
class UserInfoAdmin(admin.ModelAdmin):
    list_filter = ('title',)
admin.site.register(models.Blog)
admin.site.register(models.Category)
class ArticleAdmin(admin.ModelAdmin):
    list_filter = ('title',)
admin.site.register(models.Article,ArticleAdmin)
admin.site.register(models.UpAndDown)
admin.site.register(models.Comment)
class ClassesRecodeAdmin(admin.ModelAdmin):
    list_filter = ('class_name',)
admin.site.register(models.ClassesRecode,ClassesRecodeAdmin)
