import requests
import time
import json

class Cashier:
    headers = {
        'Cookie': "_xsrf=2|38f0a2e1|dfc607a554df1c8a6b3d9a0a20e55d56|1560909123; passport_hash=" + "2|1:0|10:1561797546|13:passport_hash|44:ZGM3MGFlNWRlZWI1MDUzMGY0OGE0MDRkNzgzYWJkODI=|0a7b5201fa650cac1225f4b0fd6d244e326ca4d9fd5d14bc900bb92790926b76" + "; passport=2|1:0|10:1561797546|8:passport|24:NDUzMDIwNHwxNTYxNzk3NTQ2|9cae89e4544551eec6d7b461331b4da38c1b9bb124d75bba18725f003c3b446a; boss_fontsize_show_type=2; boss_data_show_type=1; boss_storagelist_show_type=1; Hm_lvt_0f18425e4dfbeacd7a507a2d6e82e76c=1561597329,1561684209,1561789248,1561944317; pfshop_id=2|1:0|10:1561944718|9:pfshop_id|4:NzI4|4027a599f4dc5a35cfe0a85ec9290eda7b9d9e47a56d685ed10efe6c631ef685; Hm_lpvt_0f18425e4dfbeacd7a507a2d6e82e76c=1561944726",
        'user-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }

    login_headers = {
       'Content-Type':"application/json"
    }

    salers_body = {
                      "action": "add_records",
                      "data": [
                        {
                          "goods_id": "9150",
                          "goods_name": "货品A",
                          "supplier_id": "0",
                          "fact_price": "10",
                          "commission_mul": "10",
                          "sales_num": 0,
                          "commission": "0",
                          "deposit": "0",
                          "receipt_money": "100",
                          "salesman_id": "156",
                          "salesman_name": "这是真实姓名姓名姓名姓名",
                          "remark": "",
                          "customer_id": 0,
                          "purchase_id": 0,
                          "storage_unit_id": 15875,
                          "sale_unit_id": 15875
                        }
                      ],
                      "strict_mode": True,
                      "precision_scene": 1,
                      "precision": 3,
                      "precision_type": 1,
                      "scene_source": 1,
                      "submit_order": False,
                      "kg_upgrade": 1,
                      "_xsrf": "2|b97ecb33|e7f957a984c6be4ed6480a5314a5a561|1587347787"
                    }
    payment_body ={
                      "accountant_id": "156",
                      "total_price": "100",
                      "fact_total_price": "100",
                      "sale_record_ids": [
                        641785
                      ],
                      "precision": 3,
                      "precision_scene": 1,
                      "precision_type": 1,
                      "customer_id": 0,
                      "local_print": 0,
                      "front_end_pay_id": "LS158 937 016 020 5",
                      "last_update_timestamp": "1589370200307",
                      "erase_money": 0,
                      "erase_remark": "",
                      "goods_receipt": 0,
                      "accountant_receipt": 0,
                      "phone": "",
                      "send_sms": 0,
                      "is_refund": 0,
                      "purchase_id": 0,
                      "ifprint_order": False,
                      "source": "accountant",
                      "log": "{}",
                      "remark": "",
                      "scene_source": 1,
                      "actual_payment": "100",
                      "change_amount": "0",
                      "balance_in": "0",
                      "action": "pay_order",
                      "fund_account_id": "811",
                      "_xsrf": "2|6a995eff|341ec26557212b8205af9f9fc74230ad|1587347787"
                    }



    def __init__(self):
        pass

    def login(self):
        login_url = "http://pftest.senguo.me/login"
        headers = Cashier.login_headers
        login_body = {
            "action": "phone_password",
            "phone": "18162664593",
            "password": "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92",
            "_xsrf": "2|9b2d8870|c5aa14eaa695fd0df41b491036f6e622|1587347787"
        }
        salers_response = requests.post(login_url, data=json.dumps(login_body), headers=headers)
        time.sleep(0.5)
        cookies = salers_response.cookies.get_dict()
        cookies['sp_id']= 104
        cookies['pf_shop_id']='2|1:0|10:1588999977|9:pfshop_id|4:MTA0|e93bf861da527f80bf08d7f3867a22d9e6212e09404d21d092aab7cafed1fc9a'

        cookies_str = str("passport_hash="+cookies['passport_hash']+"; passport="+cookies['passport']+ "; pfshop_id=2|1:0|10:1589342767|9:pfshop_id|4:Mjc2|4e89d7e4c970b1660e49dd635c4ab450c7cf312e801b0cbfebcb0c48895ac7ca; sp_id=276; ")


        #print(json.dumps(cookies))
        headers = {
            'Cookie':str(cookies_str),
            'user-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'Content-Type':"application/json"

        }

        real_headers = {
            'Cookie':'_xsrf=2|11dc6bba|348abe374c7ed4bbc90cc99b93c62389|1588999956; Hm_lvt_0fed1c2b6a038e0222b7f89ea22286dc=1588999956; passport_hash="2|1:0|10:1588999975|13:passport_hash|44:ODFlZWJmZDcwMWE4MDg2YTNjNGQ1YjAwNTRmMTMwYjg=|c4e38458ee2aab20984a63c9ca3279bd4deb86e651937278b58f5ac970afa870"; passport=2|1:0|10:1588999975|8:passport|16:M3wxNTg4OTk5OTc1|8d0bee91bd5cc184869b5bc82b4826038c4bd8de34dd06309aeb5a1307ec343d; pfshop_id=2|1:0|10:1588999977|9:pfshop_id|4:MTA0|e93bf861da527f80bf08d7f3867a22d9e6212e09404d21d092aab7cafed1fc9a; sp_id=104; Hm_lpvt_0fed1c2b6a038e0222b7f89ea22286dc=1588999982',
            'user-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'Content-Type': "application/json"
        }
        return headers

