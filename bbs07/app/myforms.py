#书写用户forms表单
from django import forms
from app import models

#利用Form设置input
#widget可以设置input框样式参数
class MyRegForm(forms.Form):
    username = forms.CharField(label='用户名',min_length=3,max_length=8,
        error_messages={'register':'用户名不能为空',
                        'min_length':'用户名不能少于3位',
                        'max_length':'用户名不能多于8位'},
        widget =  forms.widgets.TextInput(attrs={'class':'form-control'})
    )
    password = forms.CharField(label='密码', min_length=3, max_length=8,
        error_messages={'register':'密码不能为空',
                        'min_length':'密码不能少于3位',
                        'max_length':'密码不能多于8位'},
        widget =  forms.widgets.PasswordInput(attrs={'class':'form-control'})
    )
    confirm_password = forms.CharField(label='确认密码', min_length=3, max_length=8,
        error_messages={'register':'确认密码不能为空',
                        'min_length':'确认密码不能少于3位',
                        'max_length':'确认密码不能多于8位'},
        widget =  forms.widgets.PasswordInput(attrs={'class':'form-control'})
    )
    email = forms.CharField(label='邮箱',
        error_messages={'register':'邮箱不能为空',
                        'invalid':'邮箱格式不正确',},
        widget =  forms.widgets.EmailInput(attrs={'class':'form-control'})
    )

    #钩子函数
    #局部钩子，校验用户名是否已存在
    def clean_username(self):
        username = self.cleaned_data.get('username')
        #去数据库校验
        is_exist = models.UserInfo.objects.filter(username=username)
        if is_exist:
            self.add_error('username','用户名已存在')
        return username

    #全局钩子，校验两次密码是否一致
    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if not password==confirm_password:
            self.add_error('confirm_password','两次输入的密码不一致')
        return self.cleaned_data

