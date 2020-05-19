import operator
import unittest
import requests
import json
import sys
import logging

from config.config import data_path

sys.path.append("../..")  # 提升2级到项目根目录下

from lib.read_excel import *  # 从项目路径下导入
from lib.case_log import log_case_info, os, log_info  # 从项目路径下导入


class BaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
         cls.data_list = excel_to_list((os.path.join(data_path, "test_user_data.xlsx")), "TestUserReg")

    def get_case_data(self, case_name):
        return get_test_data(self.data_list, case_name)

    def send_request(self, case_data):

        case_name = case_data.get('case_name')
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')
        method = case_data.get('method')
       # data_type = case_data.get('data_type')

        headers = {
            'Cookie':"_xsrf=2|38f0a2e1|dfc607a554df1c8a6b3d9a0a20e55d56|1560909123; passport_hash="+"2|1:0|10:1561797546|13:passport_hash|44:ZGM3MGFlNWRlZWI1MDUzMGY0OGE0MDRkNzgzYWJkODI=|0a7b5201fa650cac1225f4b0fd6d244e326ca4d9fd5d14bc900bb92790926b76"+"; passport=2|1:0|10:1561797546|8:passport|24:NDUzMDIwNHwxNTYxNzk3NTQ2|9cae89e4544551eec6d7b461331b4da38c1b9bb124d75bba18725f003c3b446a; boss_fontsize_show_type=2; boss_data_show_type=1; boss_storagelist_show_type=1; Hm_lvt_0f18425e4dfbeacd7a507a2d6e82e76c=1561597329,1561684209,1561789248,1561944317; pfshop_id=2|1:0|10:1561944718|9:pfshop_id|4:NzI4|4027a599f4dc5a35cfe0a85ec9290eda7b9d9e47a56d685ed10efe6c631ef685; Hm_lpvt_0f18425e4dfbeacd7a507a2d6e82e76c=1561944726",
            'user-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }

        expect_res = json.loads(expect_res)
        data = json.loads(data)
        if method.upper() == "GET":
            res = requests.get(url=url, data=data, headers=headers)
        elif method.upper() == "POST":
            res = requests.post(url=url, data=data, headers=headers)
        reponse_text = json.loads(res.text)
        if operator.eq(reponse_text, expect_res):
            result = "测试通过"
        else:
            result = "测试失败"

        log_case_info('test_accountant_cost_avg_price', url, data, expect_res, reponse_text, result)
        self.assertEqual(reponse_text, expect_res)  # 断言

if __name__ == "__main__":
    unittest.main()
    print(issubclass(BaseCase,BaseCase))