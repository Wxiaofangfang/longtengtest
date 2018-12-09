import unittest
import requests
import json
from lib import db
from lib import load_data
from conf import config

class TestUserLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls): #整个测试类的测试准备方法
        cls.sheet = load_data.get_sheet(config.data_path,"登录")

    @unittest.skipUnless(db.check_user("消防队1202"), "跳过该测试用例")
    def test_user_login_normal(self):
        case_data = load_data.get_case(self.sheet,"test_user_login_normal")
        url = case_data[2]
        data = json.loads(case_data[3]) #列表中取出的数据为字符串格式，这里需要json格式的数据，所以需要反序列化
        res = requests.post(url=url, data=data)
        self.assertIn("登录成功", res.text)

    def test_user_login_password_wrong(self):
        case_data = load_data.get_case(self.sheet,"test_user_login_password_wrong")
        url = case_data[2]
        data = json.loads(case_data[3])
        res = requests.post(url=url, data=data)
        self.assertIn("用户名或密码错误", res.text)

if __name__ == "__main__":
    unittest.main(verbosity=2)