from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header
import random



class SendEmail:

    def __init__(self,receiver):
        self.sender = "3029202939@qq.com" # 发送者QQ邮箱
        self.receiver = receiver # 接收者邮箱
        self.password = "vjftplgcqsqbdcfe"
        self.subject = "福州大学计算机院校庆网站用户验证码"


    def load_message(self):
        verification_code = self.generate_verification()
        text = f'验证码为：{verification_code}'
        message = MIMEText(text, "plain", "utf-8") # 文本内容，文本格式，编码
        message["Subject"] = Header(self.subject, "utf-8") # 邮箱主题
        message["From"] = Header(self.sender, "utf-8") # 发送者
        message["To"] = Header(self.receiver, "utf-8") # 接收者
        return message,verification_code

    def send_email(self):
        message,verification_code = self.load_message()
        smtp = SMTP_SSL("smtp.qq.com")  #需要发送者QQ邮箱开启SMTP服务
        smtp.login(self.sender, self.password)
        smtp.sendmail(self.sender, self.receiver, message.as_string())
        return verification_code

    # 生成6位随机数验证码
    def generate_verification(self):
        random_list = list(map(lambda x:random.randint(0,9),[y for y in range(6)])) # 这里使用map函数跟lambda匿名函数来生成随机的六位数
        code = "".join('%s' % i for i in random_list)
        return code

#调用
#receiver里放上发送对象的邮箱
verification = SendEmail(receiver='236238@qq.com').send_email()
print(verification)
