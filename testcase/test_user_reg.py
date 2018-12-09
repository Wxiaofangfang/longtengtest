import unittest
import requests
import json
from lib import db
from lib import load_data
from conf import config
from lib import case_log


class TestUserReg(unittest.TestCase):

    @classmethod
    def setUpClass(cls): #测试准备方法，整个测试类只执行一次
        cls.sheet = load_data.get_sheet(config.data_path,"注册")

    def test_user_reg_normal(self):
        case_data = load_data.get_case(self.sheet,"test_user_reg_normal")
        NAME = "消防队1202"
        if db.check_user(NAME):  # 环境准备，检查数据是否存在
            db.del_user(NAME)
        url = case_data[2]
        data = json.loads(case_data[3])
        excepted = json.loads(case_data[4]) #预期结果
        res = requests.post(url=url, json=data)

        # try:
        #     data = json.loads(case_data[3])
        #     excepted_res = json.loads(case_data[4])
        # except json.decoder.JSONDecodeError as e:
        #     config.logging.error("用例数据不是合法json")
        #
        # res = requests.post(url=url, json=data)
        # log_case_info("test_user_reg_normal", url, case_data[3], case_data[4], res.text)
        # try:
        #     res_json = res.json()
        # except json.decoder.JSONDecodeError as e:
        #     config.logging.error("返回结果不是json格式")

        case_log.log_case_info("test_user_reg_normal",url,case_data[3],case_data[4],res.text)

        self.assertEqual("成功", res.json()["msg"])
        self.assertDictEqual(excepted,res.json())
        self.assertTrue(db.check_user(NAME))
        db.del_user(NAME)   # 环境清理

    def test_user_reg_use_exist(self):
        case_data = load_data.get_case(self.sheet,"test_user_reg_use_exist")
        url = case_data[2]
        data = json.loads(case_data[3])
        excepted = json.loads(case_data[4])
        res = requests.post(url=url, json=data)
        self.assertEqual("失败，用户已存在", res.json()["msg"])
        self.assertDictEqual(excepted,res.json())