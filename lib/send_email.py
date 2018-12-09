# 1.组装邮件正文
# 2.组装邮件头
# 3.连接smtp服务器并发送

import smtplib #连接smtp服务器并发送
from email.mime.text import MIMEText #纯文本格式
from email.mime.multipart import MIMEMultipart #混合格式,文本和附件
from conf import config

def send_report():
    # 邮件正文
    email_body = MIMEText(config.body,"plain","utf-8")  #plain:纯文本,也可以是html
    msg = MIMEMultipart() #混合格式消息体
    msg.attach(email_body) #将正文添加到msg对象中

    msg["From"] = config.sender
    msg["To"] = config.receiver
    msg["Subject"] = config.subject

    # 附件
    with open(config.rep_path,"rb") as f:
        att_file = f.read()
    att = MIMEText(att_file,"base64","utf-8")
    att["Content.Type"] = "application/octet-stream" #声明附件的内容格式 MIME数据流格式
    att["Content-Disposition"] = "attachment;filename ='report.html'" #附件描述信息filename是附件显示的文件名
    msg.attach(att) #将附件添加到消息对象中

    smtp = smtplib.SMTP_SSL(config.smtp_server)  #建立连接
    smtp.login(config.sender,config.sender_password)
    smtp.sendmail(config.sender,config.receiver,msg.as_string())

Is_send_report =True

if __name__ == "__main__":
    send_report()