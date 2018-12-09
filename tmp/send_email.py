# 1.组装邮件正文
# 2.组装邮件头
# 3.连接smtp服务器并发送

import smtplib #连接smtp服务器并发送
from email.mime.text import MIMEText #纯文本格式
from email.mime.multipart import MIMEMultipart #混合格式,文本和附件

# 邮件正文
email_body = MIMEText("python发送的邮件","plain","utf-8")  #plain:纯文本,也可以是html
msg = MIMEMultipart() #混合格式消息体
msg.attach(email_body) #将正文添加到msg对象中

# # 组装邮件头
# email_body["From"] = "1142109981@qq.com"
# email_body["To"] = "963570929@qq.com"
# email_body["Subject"] = "from python"  #主题

msg["From"] = "1142109981@qq.com"
msg["To"] = "963570929@qq.com"
msg["Subject"] = "from python"

# 附件
with open("../report/report.html","rb") as f:
    att_file = f.read()
att = MIMEText(att_file,"base64","utf-8")
att["Content.Type"] = "application/octet-stream" #声明附件的内容格式 MIME数据流格式
att["Content-Disposition"] = "attachment;filename ='report.html'" #附件描述信息filename是附件显示的文件名
msg.attach(att) #将附件添加到消息对象中

#连接smtp服务器并发送
# smtp = smtplib.SMTP_SSL("smtp.qq.com")  #建立连接
# smtp.login("1142109981@qq.com","wfxiiweqobzgjjhe")  #登录邮箱
# smtp.sendmail("1142109981@qq.com",
#               "963570929@qq.com",
#               email_body.as_string())

smtp = smtplib.SMTP_SSL("smtp.qq.com")  #建立连接
smtp.login("1142109981@qq.com","wfxiiweqobzgjjhe")  #登录邮箱
smtp.sendmail("1142109981@qq.com",
              "963570929@qq.com",
              msg.as_string())