import smtplib
from email.header import Header
from email.mime.text import MIMEText


class sendMail():
    """
     :param From: 发件人
    　　:param To: 收件人
    　　:param Cc: 抄送
    　　:param Title: 邮件标题
    　　:param mail_msg: 邮件内容（可以是html，或文本）
    　　:return:
    """

    def SendMail(self,To, Title, mail_msg, From="18120416052@163.com", Cc=None):

        message = MIMEText(mail_msg, 'html', 'utf-8')
        message['From'] = From
        message['To'] = To

        mail_host = "smtp.163.com"  # 设置服务器
        mail_user = "18120416052@163.com"  # 用户名
        mail_pass = "JODBGWOVNHNQJLFH"  # 口令
        if Cc is not None:
           # message['Cc'] = Header("; ".join(Cc))
            message['Subject'] = Header(Title,"utf-8")
            #message['Subject'] = Title
            try:
                print(type(message))
                smtpObj = smtplib.SMTP()
                smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
                smtpObj.login(mail_user, mail_pass)
                smtpObj.sendmail(From, To, message.as_string())
                print("邮件发送成功")
            except smtplib.SMTPException:
                print("Error: 无法发送邮件")
    def send(self):

        file_name = '/Users/edz/Desktop/api_test_pf/report.html'
        f = open(file_name)
        message = f.read()
        f.close()
        receiver = "458548791@qq.com"
        cc = [""]


        self.SendMail(To=receiver,Title="测试报告",mail_msg=message,Cc = cc)


if __name__ == "__main__":
    sendMsg = sendMail()
    sendMsg.send()

