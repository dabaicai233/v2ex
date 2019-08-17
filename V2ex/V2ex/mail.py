import smtplib
import time
from email.header import Header
from email.mime.text import MIMEText

class MessageEmail():
    def __init__(self):
        # 设置服务器所需信息
        # 163邮箱服务器地址
        self.mail_host = 'smtp.163.com'
        # 163用户名
        self.mail_user = 'ldd2272096201@163.com'
        # 密码(部分邮箱为授权码)
        self.mail_pass = 'ldd2272096201'
        # 邮件发送方邮箱地址
        self.sender = 'ldd2272096201@163.com'
        # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
        self.receivers = ['diyuhuan@163.com']




    def sendMail(self, content):
        # 登录并发送邮件
        message = MIMEText(content, 'html', 'utf-8')
        # 邮件主题
        message['Subject'] = Header('今日'+time.strftime('%Y-%m-%d %H:%M') + ' v2ex tops','utf-8')
        # 发送方信息
        message['From'] = self.sender
        # 接受方信息
        message['To'] = self.receivers[0]

        try:
            # smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)
            smtpObj = smtplib.SMTP(self.mail_host)

            smtpObj.debuglevel = 1
            # 连接到服务器
            # 登录到服务器
            smtpObj.login(self.mail_user, self.mail_pass)
            # 发送
            smtpObj.sendmail( self.sender, self.receivers, message.as_string())
            # 退出
            smtpObj.quit()
            print('success')
        except smtplib.SMTPException as e:
            print('error', e)  # 打印错误

# if __name__ == '__main__':
#     mail = MessageEmail()
#     mail.sendMail('<html><h1>django 1.0 </h1><p>我的五福靈</p></html>')
#     print(time.strftime('%Y-%m-%d %H:%M') + ' v2ex tops')