#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "18120416052@163.com"  # 用户名
mail_pass = "JODBGWOVNHNQJLFH"  # 口令

sender = '18120416052@163.com'
receivers = '458548791@qq.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('为什么识别为拉近信息呢', '安赛飞', 'utf-8')
message['From'] = sender
message['To'] = receivers

subject = '测试'
message['Subject'] = Header(subject, 'utf-8')




smtpObj = smtplib.SMTP()
smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
smtpObj.login(mail_user, mail_pass)
smtpObj.sendmail(sender, receivers, message.as_string())
print("邮件发送成功")
