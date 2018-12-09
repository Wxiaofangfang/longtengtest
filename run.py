import unittest
from lib.HTMLTestRunner_PY3 import HTMLTestRunner
from lib import send_email
import conf.config


# 遍历指定文件夹下及子包下的所有测试用例  test_
all = unittest.defaultTestLoader.discover("./testcase")


if __name__ == "__main__":
    # unittest.TextTestRunner(verbosity=2).run(all)  # 两个不能同时使用
    conf.config.logging.info("测试开始"+"="*100)
    with open(conf.config.rep_path, "wb") as f:  # 二进制写模式
        HTMLTestRunner(stream=f, title="User接口测试报告", description="测试报告").run(all)
    if send_email.Is_send_report == True:
        send_email.send_report()
        conf.config.logging.info("邮件发送成功")

    conf.config.logging.info("测试结束"+"=" * 100)