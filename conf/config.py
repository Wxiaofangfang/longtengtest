
# 数据库配置
db_host = '115.28.108.130'
db_port = 3306
db_user = 'test'
db_password = '123456'
db = 'api_test'

# 路径配置，在项目中一般使用绝对路径
import os
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 数据文件目录，os.path.join()路径连接方法
data_path = os.path.join(project_path,"data","data.xlsx")
# 日志文件的目录
log_path = os.path.join(project_path,"log","log.txt")
# 报告文件目录
rep_path = os.path.join(project_path,"report","report.html")


if __name__ == "__main__":
    # 当前文件的路径
    print(os.path.abspath(__file__))
    # 当前文件文件夹的路径
    print(os.path.dirname(os.path.abspath(__file__)))
    # 项目的路径
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# log配置
import logging
# 大于等于指定级别的都可以输出,filemode="a"为新加,filemode="w"为覆盖
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(funcName)s [%(filename)s-%(lineno)d] %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename=log_path,
                    filemode="a")

# if __name__ == "__main__":
#     logging.info("hello word")
#     logging.info("中文日志")

# 邮件配置
smtp_server = "smtp.qq.com"
sender = "1142109981@qq.com"
sender_password = "wfxiiweqobzgjjhe"

receiver = "963570929@qq.com"
subject = "接口测试报告"
body = "hi,all\n附件中是接口测试报告，请查收。"
